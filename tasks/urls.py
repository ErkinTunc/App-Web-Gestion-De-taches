from django.contrib import admin
from django.urls import path
from . import views

app_name = "task"

urlpatterns = [
    
    # Home Page
    path("", views.index, name="index"), # we remoed it because we wont create other applications 
        # In here if we want to show URL like this"/index"  
        # we write like this
        # if not leave a blank "".

    # Users
    path("users/<int:user_id>/", views.detail_user, name="detail_user"), # ex:  /user/1
    path("users/add", views.create_user, name="create_user"),
    path("users/update/<int:id>/", views.update_user, name="update_user"),
    path("users/delete/<int:id>/", views.delete_user, name="delete_user"),
    
    # Teams
    path("teams/<int:team_id>/", views.detail_team, name="detail_team"), # ex: /team/1
    path("teams/add", views.create_team, name="create_team"),
    path("teams/update/<int:id>/", views.update_team, name="update_team"),
    path("teams/delete/<int:id>/", views.delete_team, name="delete_team"),
    
    # Tasks
    path("tasks/<int:task_id>/", views.detail_task, name="detail_task"), # ex: /task/1
    path("tasks/add", views.create_task, name="create_task"),
    path("tasks/update/<int:id>/", views.update_task, name="update_task"),
    path("tasks/delete/<int:id>/", views.delete_task, name="delete_task"),


    
    # Hellow World URL
    # path("item/",views.item,name="item"),
]