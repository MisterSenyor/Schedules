from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Schedule, ClientUser
from random import randint
from .models import *
from .forms import NewTaskForm, UserCreationForm, UserLogInForm
from django.contrib.auth import logout as user_logout, login as user_login, authenticate
from django.utils.timezone import now, timedelta

# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        context = {
        'range3_10': range(3, 11),
        'range1_10': range(1, 11),
        'tasks': Task.objects.filter(schedule_class__in=user.classes.all()),
        'lim': 6,
        'classes': user.classes.all(),
        'user': user,
        'form': None,
        # 'school': user.classes.first().schedule.first().school.first()
        }
        if request.GET.get('menuTaskNum'):
            context['lim'] = int(request.GET.get('menuTaskNum')) + 1
        if request.method == 'POST':
            form = NewTaskForm(request.POST)
            if form.is_valid() and request.POST.get('schedClass'):
                data = form.cleaned_data
                schedClass = int(request.POST.get('schedClass'))
                sched_class = ScheduleClass.objects.filter(id=schedClass)[0]
                date = data["date"]
                # section that calcs the date for the time left till next lesson if they choose that option
                if request.POST.get('numTillClass') != 'Select one':
                    num_days = 0
                    num_till_class = int(request.POST.get('numTillClass'))
                    sched = user.schedule.first()
                    days = [
                        sched.day2.all().filter(id=sched_class.id),
                        sched.day3.all().filter(id=sched_class.id),
                        sched.day4.all().filter(id=sched_class.id),
                        sched.day5.all().filter(id=sched_class.id),
                        sched.day6.all().filter(id=sched_class.id),
                        None,
                        sched.day1.all().filter(id=sched_class.id)
                    ]
                    i =  now().weekday()
                    while(num_till_class >= 0):
                        temp_test = days[i % 7]
                        if temp_test:
                            num_till_class -= 1
                        num_days += 1
                        i += 1
                    date = now() + timedelta(days=num_days)
                    print(date.weekday())
                    
                task = Task(
                task=data["task"], date=date,
                # school=School.objects.filter(name=request.GET.get('school')).first()
                )
                task.save()
                task.school.add(School.objects.first())
                task.schedule_class.add(sched_class)
        else:
            form = NewTaskForm()
        context["form"] = form
    else:
        return HttpResponseRedirect('/signUp')
    return render(request, 'schedules/home.html', context)


def your_school(request):

    context = {

    }
    return render(request, 'schedules/yourSchool.html', context)

def main_profile(request):

    context = {
        'schools': School.objects.filter(),
        'user': request.user,
    }
    return render(request, 'schedules/profile/myProfileMain.html', context)

def logout(request):
    if request.user.is_authenticated:
        user_logout(request)
        return HttpResponseRedirect('http://127.0.0.1:8000/')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            postdata = request.POST.copy()
            username = postdata.get('username', '')
            password = postdata.get('password', '')
            user = form.save()
            homeroomClass = request.POST.get('homeroomClass')
            for i in HomeroomClass.objects.filter(name__exact=homeroomClass).first().classes.all():
                user.classes.add(i)
            user.set_password(password)
            user.save()
            user = authenticate(
                username=username,
                password=password
            )
            user_login(request, user)
            print(password)
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form = UserCreationForm()
    form.fields['classes'].queryset = ScheduleClass.objects.filter(homeRoom__exact=False)
        # TODO - make homeroomclassses sort by the schedule chosen
    return render(request, 'schedules/signup/signup.html', {'form':form, 'homeroomClasses': HomeroomClass.objects.all()})

def login(request):
    if request.method == 'POST':
        form = UserLogInForm(request.POST)
        if form.is_valid():
            postdata = request.POST.copy()
            username = postdata.get('username', '')
            password = postdata.get('password', '')
            try:
                user = authenticate(
                    username=username,
                    password=password
                )
                user_login(request, user)
            except:
                pass
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form = UserLogInForm()
    return render(request, 'schedules/login.html', {'form':form})

def tasks(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    context = {
        'fields': Task._meta.get_fields(),
        'tasks': Task.objects.filter(schedule_class__in=user.classes.all())
    }
    if request.GET.get('fieldSelect'):
        context['field'] = request.GET.get('fieldSelect')
    else:
        context['field'] = 'id'
    return render(request, 'schedules/tasksView.html', context)