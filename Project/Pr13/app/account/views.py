from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm, ProfileForm
from django.http import HttpRequest
from .models import Profile
from django.contrib.auth.decorators import login_required

def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', context={
        'title': 'Регистрация',
        'form': form,
    })

def login_user(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', context={
        'title': 'Авторизация',
        'form': form,
    })

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile_view(request: HttpRequest):
    user = Profile.objects.select_related('user').get(user=request.user)
    return render(request, 'profile.html', context={
        'user': user
    })

def profile_edit(request: HttpRequest):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'editProfile.html', context={
        'title': 'Профиль',
        'form': form,
    })