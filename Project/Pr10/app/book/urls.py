from django.contrib import admin
from django.urls import path
from .views import get_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home),
]
