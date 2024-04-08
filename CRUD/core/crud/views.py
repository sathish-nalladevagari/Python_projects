from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html' , {})

def register_user(request):
    return render(request, 'register.html' , {})

def login_user(request):
    return render(request, 'login.html' , {})