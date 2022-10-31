from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'age', 'date_of_birth']
    ordering = ['-created']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['-title']
