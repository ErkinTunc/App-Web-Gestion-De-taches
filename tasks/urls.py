from django.contrib import admin
from django.urls import path
from . import views

app_name = "task"

urlpatterns = [
    
    
    # Home Page for Admin
    path("control-panel/", views.admin_index, name="admin_index"),
    
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
    path("teams/<int:team_id>/enter/<int:user_id>/", views.enter_team, name="enter_team"), # ex: /team/1/enter/7
    path("teams/<int:team_id>/leave/<int:user_id>/", views.leave_team, name="leave_team"), # ex: /team/1/leave/7
    
    # Tasks
    path("tasks/<int:task_id>/", views.detail_task, name="detail_task"), # ex: /task/1
    path("tasks/add", views.create_task, name="create_task"),
    path("tasks/update/<int:id>/", views.update_task, name="update_task"),
    path("tasks/delete/<int:id>/", views.delete_task, name="delete_task"),
    path("tasks/<int:task_id>/add-sub-task", views.create_sub_task, name="create_sub_task"),
    path("tasks/<int:task_id>/add-sub-team", views.create_sub_team, name="create_sub_team"),

    
    # Hellow World URL
    # path("item/",views.item,name="item"),
]