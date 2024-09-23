from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .models import Furniture

# Create your views here.
def get_home(requset):
    return render(requset, 'home.html')

def get_aboutUs(request):
    return render(request, 'aboutUs.html')

def get_products(request):
    products = Furniture.objects.all()
    return render(request, 'products.html', context={
        'products': products,
    })
    
def get_product_detail(request, pk):
    product = Furniture.objects.get(pk=pk)
    return render(request, 'detail_product.html', context={
        'product': product
    })
    
def search_product(request):
    if request.method == "GET":
        search = request.GET['search']
        products = Furniture.objects.filter(
            Q(label__icontains = search))
        return render(request, template_name='products.html', context={
            'products': products,
            'title': 'Книги'
        })
    return redirect(reverse('home'))