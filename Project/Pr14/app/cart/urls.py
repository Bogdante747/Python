from django.contrib import admin
from django.urls import path
from .views import cart_add, cart_detail, cart_remove

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', cart_detail, name="cart_detail"),
    path('create/<int:furniture_id>', cart_add, name="cart_add"),
    path('remove/<int:furniture_id>', cart_remove, name="cart_remove"),

]