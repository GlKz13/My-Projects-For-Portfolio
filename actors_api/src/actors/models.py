from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title


class Actor(models.Model):
	name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=100, db_index=True)
	age = models.IntegerField()
	date_of_birth = models.DateField(null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name + self.last_name