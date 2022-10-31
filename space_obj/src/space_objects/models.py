from django.db import models
from django.urls import reverse

# Create your models here.

class SpaceObject(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, db_index=True)
    published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-published']

    def get_absolute_url(self):

        return reverse('space_objects:obj_content', args=[self.slug])

class Category(models.Model):
    title = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(unique=True, null=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('space_objects:category_page', args=[self.slug])

class Email(models.Model):
    email = models.EmailField(unique=True)
    added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.email

