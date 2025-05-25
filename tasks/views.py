from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login # might be deleted in the future
from django.contrib import messages # might be deleted in the future
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Team , Task , UserProfile # importing from models.py Item sql table
from django.template import loader
from .forms import CustomUserForm, TeamForm,TaskForm, UserUpdateForm, UserProfileUpdateForm 

# Create your views here.
from django.http import HttpResponse

# ================= ADMIN-INDEX =====================

@login_required
def admin_index(request):
    task_list = Task.objects.all() # rn they (task_list) are objects
    team_list = Team.objects.all()
    user_list = UserProfile.objects.all()
    
    task_count = task_list.count() # count metod counts all the elements in the list
    team_count = team_list.count()
    user_count = user_list.count()
    
    # template = loader.get_template("tasks/index.html") # with the help of loader we save the html like an variable.
    context = { # we use this to create dynamique pages we use this variable as an attribute | we use the content in it like objects
        "task_list":task_list,
        "team_list":team_list,
        "user_list":user_list,
        
        "user_count": user_count,
        "team_count": team_count,
        'task_count': task_count,
        
        "current_user": request.user, # after login it contains current users information
    }
    return render(request,"admin-index.html",context)


# ================= INDEX =====================

@login_required
def index(request):
    task_list = Task.objects.all()
    team_list = Team.objects.all()
    
    current_user = request.user
    
    public_task_lists = []
    
    users_team = current_user.teams.all()
    users_task_set = set(current_user.tasks.all()) # set prevents duplication


    for team in current_user.teams.all():
        for task in team.tasks.all():
            users_task_set.add(task)

    
    # public list of tasks
    for task in task_list:
        if task.private == False :
            public_task_lists.append(task)
    
    
    context = {
        "current_user":current_user,
        "public_task_list":public_task_lists,
        "users_task_list":list(users_task_set),  # convert set to list
        "users_team":users_team
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
def detail_user(request, user_id):
    profile = UserProfile.objects.get(pk=user_id)
    context = {
        "profile": profile, 
    }
    return render(request, "users/detail.html", context)


# =================== CREATE ====================
@login_required
def create_user(request):
    form = CustomUserForm(request.POST or None)

    if request.user.is_superuser: # Only admin can create a user
        return HttpResponse("Only superusers can create new users.")

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
        task = form.save(commit=False) # Create task instance, but not saved yet
        task.creator = request.user # Set the current user as the creator
        task.save() # Save the task with the creator
        form.save_m2m() # Creating forms from models | # Save many-to-many fields (users, teams, subtasks) | if not it causes problems
        return redirect("task:index")

    return render(request, "tasks/task-form.html", {"form": form})

@login_required
def create_sub_task(request,task_id):
    
    task = Task.objects.get(id=task_id)
    # Cheking autorization
    in_any_team = False #checks if any user is in one of the teams assaigned on to the task
    for team in task.teams.all():
        if request.user in team.users.all():
            in_any_team = True

    if (not in_any_team) and (request.user != task.creator) and (request.user  not in task.users.all()) and not request.user.is_superuser: # you shall not pass (unless y are superuser or in the team)
        return HttpResponse("You are not authorized to create an sub-task for this task")

    # Creation of sub-task , (we can not use the create_task function because if we do we can not link task and sub-task)
    form = TaskForm(request.POST or None)

    if form.is_valid():
        sub_task = form.save(commit=False) 
        sub_task.creator = request.user 
        sub_task.save() 
        form.save_m2m() 
        
        # we are saving sub-task to task
        task.subtasks.add(sub_task)
        task.save()
        
        return redirect("task:index")

    return render(request, "tasks/task-form.html", {"form": form})

@login_required
def create_sub_team(request,task_id):
    
    task = Task.objects.get(id=task_id)
    # Cheking autorization
    in_any_team = False #checks if any user is in one of the teams assaigned on to the task
    for team in task.teams.all():
        if request.user in team.users.all():
            in_any_team = True

    if (not in_any_team) and (request.user != task.creator) and (request.user  not in task.users.all()) and not request.user.is_superuser: # you shall not pass (unless y are superuser or in the team)
        return HttpResponse("You are not authorized to create an sub-task for this task")

    # Creation of sub-task , (we can not use the create_task function because if we do we can not link task and sub-task)
    form = TeamForm(request.POST or None)

    if form.is_valid():
        sub_team = form.save(commit=False)
         
        sub_team.save()
        task.teams.add(sub_team) # first save team to server then add in to the task
        
        form.save_m2m()
        return redirect("task:index")

    return render(request, "teams/team-form.html", {"form": form})
    
    

# ================== UPDATE =====================

@login_required
def update_user(request, id):  # TODO: Should make it right it is creating new users
    user_profile = get_object_or_404(UserProfile, id=id)
    user = user_profile.user

    if request.user != user and not request.user.is_superuser: # you shall not pass (unless y are superuser or profileOwner)
        return HttpResponse("You are not authorized to update this profile.")


    user_form = UserUpdateForm(request.POST or None, instance=user)  # instance=user will put all the info of the user into our form
    profile_form = UserProfileUpdateForm(request.POST or None, request.FILES or None, instance=user_profile)  # extra user info && dont fotget to add 2 formats into the html page

    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save() # saving the modified data

        messages.success(request, "User has been updated!!!") 
        return redirect("task:index")  # go back to index after update

    return render(request, 'users/user-form.html', {
        'form': user_form,
        'profile_form': profile_form,
        'user': user
    })

@login_required
def update_team(request, id):
    team = Team.objects.get(id=id)
    form = TeamForm(request.POST or None, instance=team)

    
    if (request.user  not in team.users.all()) and not request.user.is_superuser: # you shall not pass (unless y are superuser or in the team)
        return HttpResponse("You are not authorized to update this profile.")

    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, 'teams/team-form.html', {'form': form, 'team': team})

@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    in_any_team = False #checks if any user is in one of the teams assaigned on to the task
    for team in task.teams.all():
        if request.user in team.users.all():
            in_any_team = True

    if (not in_any_team) and (request.user != task.creator) and (request.user  not in task.users.all()) and not request.user.is_superuser: # you shall not pass (unless y are superuser or in the team)
        return HttpResponse("You are not authorized to update this profile.")


    if form.is_valid():
        form.save()
        return redirect("task:index")

    return render(request, 'tasks/task-form.html', {'form': form, 'task': task})


# ================= DELETE =======================
@login_required
def delete_user(request, id):
    userProfile = UserProfile.objects.get(id=id)
    user = userProfile.user # userProfile and user is connected but we should delete
    # user because it is the main one and we make relations with teams and tasks with 
    # user class not with the other

    if request.user != user and not request.user.is_superuser: # you shall not pass (unless y are superuser or profileOwner)
        return HttpResponse("You are not authorized to delete this profile.")

    if request.method == 'POST':
        user.delete()
        return redirect('task:index')

    return render(request, 'users/user-delete.html', {'user': user})

@login_required
def delete_team(request, id):
    team = Team.objects.get(id=id)
    
    if (request.user  not in team.users.all()) and not request.user.is_superuser: # you shall not pass (unless y are superuser or in the team)
        return HttpResponse("You are not authorized to delete this team.")

    if request.method == 'POST':
        team.delete()
        return redirect('task:index')

    return render(request, 'teams/team-delete.html', {'team': team})

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    
    if (request.user != task.creator) and not request.user.is_superuser: # you shall not pass (unless y are superuser or in the team)
        return HttpResponse("You are not authorized to delete this. Only the creator of this task can delete it")


    if request.method == 'POST':
        task.delete()
        return redirect('task:index')

    return render(request, 'tasks/task-delete.html', {'task': task})

# ================= Enter ==========================
@login_required
def enter_team(request, team_id, user_id):
    
    user_profile = get_object_or_404(UserProfile, id=user_id)
    user = user_profile.user
    
    team = get_object_or_404(Team, id=team_id)
    
    if request.method == 'POST': # Django doesnt support PATCH --> use POST instead
        team.users.add(user) # added user to the team
        team.save()
        return redirect('task:detail_team', team_id=team.id) 
    
    # for GET
    return redirect('task:detail_team', team_id=team.id)
    
# ================= Leave ==========================

@login_required
def leave_team(request, team_id, user_id):
    
    user_profile = get_object_or_404(UserProfile, id=user_id)
    user = user_profile.user
    team = Team.objects.get(id=team_id)
    
    if request.method == 'POST':
        
        try:
            team.users.remove(user) # added user to the team
        except ValueError:
            print("There is a problem while leaving from team with <" + team_id + "> team id")
        team.save()
        return redirect('task:detail_team', team_id=team.id)
    
    # for GET
    return redirect('task:detail_team', team_id=team.id)

# ================= HELLO WORLD ==========================

# @login_required # we do not need and login_required this method does nothing.
def item(request):
    return HttpResponse("<h1>This is an item view</h1>")
    # we don't realy need to do this we can add html files with templates
    # this is not the proper way 




