from django.shortcuts import render , redirect
from .forms import RegisterForm , TodoForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .models import Todo
from django.http import Http404

# Create your views here.


def index(request):
	if request.user.is_authenticated:
		todolist = Todo.objects.filter(user = request.user)
		return render(request, 'home.html' , {'todolist':todolist})
	return redirect('login')

#Register

def register_user(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username , password = password)
			if user is not None:
				login(request,user)
				messages.success(request, "User created")
				return redirect('home')
	else:
		form = RegisterForm()
		return render(request, 'register.html' , {'form' : form})
	return render(request, 'register.html' , {'form':form})
               
#Login            

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#Authenticate
		user = authenticate(request, username = username , password = password)
		if user is not None:
			login(request, user)
			messages.success(request, "Login Success")
			return redirect('home')
		else:
			messages.success(request, "Login failed")
			return redirect('login')
	return render(request, 'login.html')


# Logout

def logout_user(request):
	logout(request)
	messages.success(request, "You have logged out")
	return redirect('home')


# Add new task

def add_task(request):
	if request.method == "POST":
		print(request.user)
		form = TodoForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.user = request.user
			item.save()

			messages.success(request, "New Task added")
			return redirect('home')
	else:	
		form = TodoForm()
		return render(request, 'addtask.html', {'form':form})

def update_task(request , pk):
	try:
		task_data = Todo.objects.get(id = pk, user = request.user)
	except Todo.DoesNotExist:
		raise Http404("The id is not is user database")
		
	if request.method == 'POST':
		form = TodoForm(request.POST or None , instance=task_data)
		if form.is_valid():
			form.save()
			messages.success(request , "Task Updated Success")
			return redirect('home')
	else:
		form = TodoForm(instance= task_data)
		return render(request, 'update_task.html' ,{'form':form})

