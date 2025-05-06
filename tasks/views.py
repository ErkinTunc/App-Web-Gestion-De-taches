from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Team , Task , UserProfile # importing from models.py Item sql table
from django.template import loader
from .forms import CustomUserForm, TeamForm,TaskForm

# Create your views here.
from django.http import HttpResponse

# ================= INDEX =====================
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

def detail_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        "task":task,
    }
    return render(request,"tasks/detail.html",context)

def detail_team(request,team_id):
    team = Team.objects.get(pk=team_id)
    context = {
        "team":team,
    }
    return render(request,"teams/detail.html",context)

def detail_user(request,user_id):
    user = UserProfile.objects.get(pk=user_id)
    context = {
        "user":user,
    }
    return render(request,"users/detail.html",context)


# =================== CREATE ====================
def create_user(request):
    form = CustomUserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, "users/user-form.html", {"form": form})


def create_team(request):
    form = TeamForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, "teams/team-form.html", {"form": form})


def create_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, "tasks/task-form.html", {"form": form})

# ================== UPDATE =====================
def update_user(request, id):
    user = UserProfile.objects.get(id=id)
    form = CustomUserForm(request.POST or None, instance=user.user)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, 'users/user-form.html', {'form': form, 'user': user})


def update_team(request, id):
    team = Team.objects.get(id=id)
    form = TeamForm(request.POST or None, instance=team)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, 'teams/team-form.html', {'form': form, 'team': team})


def update_task(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, 'tasks/task-form.html', {'form': form, 'task': task})


# ================= DELETE =======================
def delete_user(request, id):
    user = UserProfile.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('task:index')

    return render(request, 'users/user-delete.html', {'user': user})


def delete_team(request, id):
    team = Team.objects.get(id=id)

    if request.method == 'POST':
        team.delete()
        return redirect('task:index')

    return render(request, 'teams/team-delete.html', {'team': team})


def delete_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task:index')

    return render(request, 'tasks/task-delete.html', {'task': task})


# ================= HELLO WORLD ==========================

def item(request):
    return HttpResponse("<h1>This is an item view</h1>")
    # we don't realy need to do this we can add html files with templates
    # this is not the proper way 




