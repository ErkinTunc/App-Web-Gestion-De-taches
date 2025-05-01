from django import forms 
from .models import UserProfile,Team,Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm): # this will ask user 2 times its password and hash it
    class Meta:
        model = User
        fields = ['username', 'email']

class TeamForm(forms.ModelForm):
        class Meta: # a meta class which will hold the data
            model = Team
            fields = ['name',"users"]

class TaskForm(forms.ModelForm):
        class Meta: # a meta class which will hold the data
            model = Task
            fields = ["title","status","description","users","teams","subtasks","deadline"]
