from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm
from django.http import HttpRequest
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from order.models import OrderItem
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

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
def profile_view(request: HttpRequest, pk):
    if pk != request.user.id:
        return redirect('home')
    user = Profile.objects.select_related('user').get(user=pk)
    orderItem = OrderItem.objects.select_related('order').filter(order__customer_user_id=pk)
    return render(request, 'profile.html', context={
        'user': user,
        'orderItem': orderItem
    })

class profile_edit(UpdateView):
    model = Profile
    template_name='editProfile.html'
    fields = ['country', 'city', 'street', 'house', 'apartment_number', 'gender']
