from django.contrib import admin
from django.urls import path
from .views import create_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_order, name='create_order'),
]
