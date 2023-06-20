
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import User

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login') 
    return wrapper

def sales_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'user':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login') 
    return wrapper

def teamleader_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'tl':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  
    return wrapper