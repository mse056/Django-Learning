from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            user.first_name = data['firstname']
            user.last_name = data['lastname']
            user.save()
            messages.success(request, 'user registered', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'user logged in successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'username of password is incorrect', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})

def user_logout(request):
    logout(request)
    messages.warning(request, 'user logged out successfully', 'warning')
    return redirect('home')
