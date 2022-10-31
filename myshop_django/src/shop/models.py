from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField(unique=True)
	class Meta:
		ordering =['name']


	def __str__(self):
		return self.name

	def get_absolure_url(self):
		return reverse("shop:product_list_by_category", args=[self.slug])




class Product(models.Model):
	cat = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	description = models.TextField(null=True)
	class Meta:
		ordering =['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("shop:product_detail", args=[self.id, self.slug])

