from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegisterForm
from .decorators import unauthenticated_user

from django.contrib.auth.views import LoginView
# Create your views here.

@unauthenticated_user
def register(request):
    if(request.method == "POST"):
        form = RegisterForm(request.POST)
        if( form.is_valid() ):
            form.save() # saves the user to data base
            username = form.cleaned_data.get("username")
            messages.success(request,f"Welcome {username}, your account is created")
            return redirect("login")
    else:
        form = RegisterForm()
    return render (request, "users/register.html",{"form":form})

@unauthenticated_user
def login(request):
    
    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect("task:index")
        else:
            messages.error(request, "Username or password is incorrect")
            
    return render(request, "users/login.html")    