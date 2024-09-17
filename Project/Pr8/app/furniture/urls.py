from django.contrib import admin
from django.urls import path
from .views import get_home, get_aboutUs, get_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='home'),
    path('aboutUs/', get_aboutUs, name='aboutUs'),
    path('products/', get_products, name='products'),
]
