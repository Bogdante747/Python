from django.shortcuts import render
from .models import Furniture

# Create your views here.
def get_home(requset):
    return render(requset, 'home.html')

def get_aboutUs(request):
    return render(request, 'aboutUs.html')

def get_products(request):
    product = Furniture.objects.all()
    return render(request, 'products.html', context={
        'product': product,
    })
    
def get_product_detail(request, pk):
    product = Furniture.objects.get(pk=pk)
    return render(request, 'detail_product.html', context={
        'product': product
    })