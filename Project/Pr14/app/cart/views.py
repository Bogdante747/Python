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

def cart_clear(request: HttpRequest):
    cart = CartSession(request.session)
    cart.clear()
    return redirect(reverse('cart_detail'))

def cart_plus(request: HttpRequest, furniture_id):
    cart = CartSession(request.session)
    furniture = get_object_or_404(Furniture, id=furniture_id)
    cart.change_quantity(furniture=furniture, method="plus")
    return redirect(reverse('cart_detail'))


def cart_minus(request: HttpRequest, furniture_id):
    cart = CartSession(request.session)
    furniture = get_object_or_404(Furniture, id=furniture_id)
    cart.change_quantity(furniture=furniture, method="minus")
    return redirect(reverse('cart_detail'))
