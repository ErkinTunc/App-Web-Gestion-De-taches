from django.contrib import admin
from django.urls import path
from . import views

app_name = "task"

urlpatterns = [
    # /tasks/
    path("",views.index,name="index"), 
    # In here if we want to show URL like this"/index"  
    # we write like this
    # if not leave a blank "".

    # /tasks/1
    path("task/<int:task_id>/", views.detail_task, name="detail"),

    # Hellow World URL
    path("item/",views.item,name="item"),
]