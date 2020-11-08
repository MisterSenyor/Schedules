from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.

class School(models.Model):
    site = models.TextField(default="none")
    name = models.CharField(default="none", max_length=800)
    def __str__(self):
        return self.name


class ScheduleClass(models.Model):
    name = models.CharField(default="none", max_length=800)
    _id = models.IntegerField(default=0)
    homeRoom = models.BooleanField()
    def __str__(self):
        return self.name


class Schedule(models.Model):
    grade = models.CharField(name='grade', default='none', max_length=800)
    day1 = models.ManyToManyField(ScheduleClass, related_name="day1")
    day2 = models.ManyToManyField(ScheduleClass, related_name="day2")
    day3 = models.ManyToManyField(ScheduleClass, related_name="day3")
    day4 = models.ManyToManyField(ScheduleClass, related_name="day4")
    day5 = models.ManyToManyField(ScheduleClass, related_name="day5")
    day6 = models.ManyToManyField(ScheduleClass, related_name="day6")
    school = models.ManyToManyField(School, null=True)
    days = [day1, day2, day3, day4, day5, day6]
    def lesson_count(self):
        lessons = []
        for i in self.days:
            for j in i.split('_'):
                if j not in lessons:
                    lessons.append(j)
        return lessons
    def __str__(self):
        return self.grade


class ClientUser(AbstractUser):
    # SCHEDULE RELATED CLASSES:
    classes = models.ManyToManyField(ScheduleClass, name="classes")
    personal_changes = models.TextField(name="personal_changes", default="none")
    schedule = models.ManyToManyField(Schedule)
    def get_classes(self):
        return self.classes
    # SETTINGS RELATED FIELDS:


class Task(models.Model):
    task = models.TextField(name="task", default="none")
    schedule_class = models.ManyToManyField(ScheduleClass, name="schedule_class")
    date = models.DateField(name="date", default=now())
    school = models.ManyToManyField(School, name="school")
    def __str__(self):
        return self.task

class HomeroomClass(models.Model):
    schedule = models.ManyToManyField(Schedule)
    name = models.CharField(max_length=30)
    classes = models.ManyToManyField(ScheduleClass)
    def __str__(self):
        return self.name