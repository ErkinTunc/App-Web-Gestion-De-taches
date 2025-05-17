from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Team , Task , UserProfile # importing from models.py Item sql table
from django.template import loader
from .forms import CustomUserForm, TeamForm,TaskForm

# Create your views here.
from django.http import HttpResponse

# ================= INDEX =====================

@login_required
def index(request):
    task_list = Task.objects.all()
    team_list = Team.objects.all()
    user_list = UserProfile.objects.all()
    # template = loader.get_template("tasks/index.html") # with the help of loader we save the html like an variable.
    context = { # we use this to create dynamique pages we use this variable as an attribute | we use the content in it like objects
        "task_list":task_list,
        "team_list":team_list,
        "user_list":user_list,
    }
    return render(request,"index.html",context)

# ======================= DETAILS =====================
# leads us to details.html pages

@login_required
def detail_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        "task":task,
    }
    return render(request,"tasks/detail.html",context)

@login_required
def detail_team(request,team_id):
    team = Team.objects.get(pk=team_id)
    context = {
        "team":team,
    }
    return render(request,"teams/detail.html",context)

@login_required
def detail_user(request,user_id):
    user = UserProfile.objects.get(pk=user_id)
    context = {
        "user":user,
    }
    return render(request,"users/detail.html",context)


# =================== CREATE ====================
@login_required
def create_user(request):
    form = CustomUserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, "users/user-form.html", {"form": form})

@login_required
def create_team(request):
    form = TeamForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, "teams/team-form.html", {"form": form})

@login_required
def create_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, "tasks/task-form.html", {"form": form})

# ================== UPDATE =====================
@login_required
def update_user(request, id): #TODO: Shoudl make it right it is creating new users
    user = UserProfile.objects.get(id=id)
    form = CustomUserForm(request.POST or None, instance=user.user)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, 'users/user-form.html', {'form': form, 'user': user})

@login_required
def update_team(request, id):
    team = Team.objects.get(id=id)
    form = TeamForm(request.POST or None, instance=team)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, 'teams/team-form.html', {'form': form, 'team': team})

@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, 'tasks/task-form.html', {'form': form, 'task': task})


# ================= DELETE =======================
@login_required
def delete_user(request, id):
    user = UserProfile.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('task:index')

    return render(request, 'users/user-delete.html', {'user': user})

@login_required
def delete_team(request, id):
    team = Team.objects.get(id=id)

    if request.method == 'POST':
        team.delete()
        return redirect('task:index')

    return render(request, 'teams/team-delete.html', {'team': team})

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task:index')

    return render(request, 'tasks/task-delete.html', {'task': task})


# ================= HELLO WORLD ==========================

# @login_required # we do not need and login_required this method does nothing.
def item(request):
    return HttpResponse("<h1>This is an item view</h1>")
    # we don't realy need to do this we can add html files with templates
    # this is not the proper way 




