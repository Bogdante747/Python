from django.contrib import admin
from django.urls import path
from .views import register, login_user, logout_view, profile_view, profile_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name="register"),
    path('login/', login_user, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', profile_view, name='profile'),
    path('profile/<int:pk>/edit/', profile_edit.as_view(), name='editProfile'),
]
