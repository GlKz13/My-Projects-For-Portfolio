from django.db import models

# Create your models here.
class Color(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title

class CarBrand(models.Model):
    carBrandTitle = models.CharField(max_length=50)


    def __str__(self):
        return self.carBrandTitle

class CarModel(models.Model):
    carModelTitle = models.CharField(max_length=50)

    def __str__(self):
        return self.carModelTitle



class Order(models.Model):
    color    = models.ForeignKey(Color, on_delete=models.CASCADE)
    carModel = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    carBrand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    date     = models.DateField(auto_now_add=True)
   

    def __str__(self):
        return f'{self.carBrand}, {self.carModel},  {self.quantity} car(s), {self.date}'

