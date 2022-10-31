from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	fields = ['title']

@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
	fields = ['carBrandTitle']

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
	fields = ['carModelTitle']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	fields = ['color', 'carBrand', 'carModel', 'quantity']
	



