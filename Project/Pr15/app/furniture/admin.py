from django.contrib import admin
from furniture.models import Furniture

# Register your models here.
@admin.register(Furniture)
class AdminFurniture(admin.ModelAdmin):
    pass