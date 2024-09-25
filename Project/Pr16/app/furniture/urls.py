from django.contrib import admin
from django.urls import path
from .views import get_home, get_aboutUs, get_products, get_product_detail, search_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='home'),
    path('aboutUs/', get_aboutUs, name='aboutUs'),
    path('product/', get_products, name='products'),
    path('product/<int:pk>', get_product_detail, name='product_detail'),
    path("product/search", search_product, name="search")
]
