from django.shortcuts import render
from django.http import HttpResponse
from .models import Team , Task , UserProfile # importing from models.py Item sql table
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    task_list = Task.objects.all()
    # template = loader.get_template("tasks/index.html") # with the help of loader we save the html like an variable.
    context = { # we use this to create dynamique pages we use this variable as an attribute | we use the content in it like objects
        "task_list":task_list,
    }
    return render(request,"tasks/index.html",context)


def detail_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        "task":task,
    }
    return render(request,"tasks/detail.html",context)



def item(request):
    return HttpResponse("<h1>This is an item view</h1>")
    # we don't realy need to do this we can add html files with templates
    # this is not the proper way 




