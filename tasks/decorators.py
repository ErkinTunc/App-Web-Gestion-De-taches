from django.http import HttpResponse
from django.shortcuts import redirect


# if user is aurhenticated it returns to task:index 
#TODO : didn't work like ı expected, modify it
def allowed_users(allowed_roles=[]): 
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            # print("Working:" , allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args , **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")
        
        return wrapper_func
    return decorator
        
        
        


