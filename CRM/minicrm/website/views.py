from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.


def index(request):
    
    return render(request, 'home.html' , {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request , user)
            messages.success(request, "You have been logged in")
        else:
            messages.success(request, "You have error  logged in please try again ")
            return redirect('login.html')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')