from django.contrib import admin

# email = shop@mail.ru
#name = shop
#password = shop


# Register your models here.

from .models import *

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}
