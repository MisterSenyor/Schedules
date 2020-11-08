from django import forms
from .models import ClientUser

class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=800)
    date = forms.DateField(input_formats=['%d/%m/%Y'], required=False)

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = ClientUser
        fields = ['username', 'password', 'classes', 'schedule']

class UserLogInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=150)