from django.contrib import admin
from account.models import Profile

# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass