from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from cart.cart import CartSession
from .forms import OrderForm
from .models import OrderItem
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render



# Create your views here.
@login_required(login_url='login')
def create_order(request: HttpRequest):
    cart = CartSession(request.session)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer_user = request.user
            order.save()
            for item_cart in cart:
                OrderItem.objects.create(order=order, furniture=item_cart['furniture'], quantity=item_cart['quantity']).save()
            cart.clear()
            return redirect(reverse('home'))
    else:
        form = OrderForm()
    return render(request, 'cart_detail.html', context={
        'title': 'Заказы',
        'form': form,
    })