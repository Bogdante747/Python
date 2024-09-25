from django.shortcuts import render
from .cart import CartSession
from django.http import HttpRequest
from furniture.models import Furniture
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

def cart_add(request: HttpRequest, furniture_id):
    cart = CartSession(request.session)
    furniture = get_object_or_404(Furniture, id=furniture_id)
    cart.add(furniture=furniture)

    return redirect(reverse('cart_detail'))

def cart_remove(request: HttpRequest, furniture_id):
    cart = CartSession(request.session)
    furniture = get_object_or_404(Furniture, id=furniture_id)
    cart.remove(furniture=furniture)
    return redirect(reverse('cart_detail'))

def cart_detail(request: HttpRequest):
    cart = CartSession(request.session)
    return render(request, 'cart_detail.html', context={
        'cart': cart
    })