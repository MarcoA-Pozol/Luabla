from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import RegisterForm, LoginForm
from .models import User
from BackEnd.models import Notification

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                #Create new User
                user = form.save(commit=False)
                user.save()
                
                #Create Notification
                notification = Notification.objects.create(reason="Welcome to Luabla", message=f'Hi {user}, welcome to Luabla!. Your account has been created successfully, this is your notifications center.', destinatary=user, is_read=False)
                
                auth.login(request, user)
                return redirect('/')
            except Exception as e:
                form.add_error(None, f"Error during User creation: {e}")
                print(f"Error during User creation: {e}")
    else:
        form = RegisterForm()
        print("Form is not valid")
        print(form.errors)
        
    context = {'form':form}
    return render(request, 'register.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')