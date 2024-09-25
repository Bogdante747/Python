from django.contrib import admin
from django.urls import path
from .views import cart_add, cart_detail, cart_remove, cart_clear, cart_plus, cart_minus

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', cart_detail, name="cart_detail"),
    path('create/<int:furniture_id>', cart_add, name="cart_add"),
    path('remove/<int:furniture_id>', cart_remove, name="cart_remove"),
    path('clear/', cart_clear, name="cart_clear"),
    path('plus/<int:furniture_id>', cart_plus, name="cart_plus"),
    path('minus/<int:furniture_id>', cart_minus, name="cart_minus"),
]