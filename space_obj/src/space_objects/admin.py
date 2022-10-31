from django.contrib import admin
from .models import *

#name = admin
#login = admin@mail.ru
#password = admin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(SpaceObject)
class SpaceObjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published', 'cat']
    ordering = ['-published']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email', 'added']
    ordering = ['-added']
