from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()
    return render(request, 'home.html' , {'records' : records})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request , user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "You have error  logged in please try again ")
            return redirect('login')
    else:
          
        return render(request,'login.html')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def custromer_record(request, pk):
    if request.user.is_authenticated: 
        record = Record.objects.get(id=pk)
        return render(request, 'customer_record.html' ,{'record': record})
    else:
         messages.success(request, "You have to login to view this page")
         return redirect('home')
    
def delete_record(request, pk):
     if request.user.is_authenticated:
          recordit = Record.objects.get(id=pk)
          recordit.delete()
          messages.success(request, " you have deleted the user")
          return redirect ('home')
     else:
          messages.success(request, " you dont have access to delete the user")
          return redirect('home')
          

    