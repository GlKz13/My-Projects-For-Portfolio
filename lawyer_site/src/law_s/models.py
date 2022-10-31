from django.db import models

# Create your models here.

#password = admin
#name = admin

class Client(models.Model):
    name = models.CharField("Имя", max_length=20)
    phone = models.BigIntegerField("Номер телефона")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return (f'{self.name}, {self.phone}')
