from django.contrib import admin
from django.urls import path
from .views import register, login_user, logout_view, profile_view, profile_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path('login/', login_user),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit, name='editProfile'),
]
