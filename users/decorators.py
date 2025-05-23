from django.http import HttpResponse
from django.shortcuts import redirect


# if user is aurhenticated it returns to task:index 
def unauthenticated_user(view_func): 
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("task:index")
        else:
            return view_func(request, *args , **kwargs)# view fonction is login page
    return wrapper_func

