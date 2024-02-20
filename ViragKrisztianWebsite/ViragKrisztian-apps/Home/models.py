from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.base import Model
from datetime import datetime


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    joined_date= models.DateField(auto_now_add=True)


    def __str__(self):
        return f"name: {self.name}, email: {self.email}"

class Description(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"Description: {self.text}"

class ImageCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Name: {self.name}"
    
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='files/images')
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=5000)
    
    def __str__(self):
        return f"'name':{self.name}, 'image':{self.image}, 'category':{self.category.name}, 'description': {self.description}"

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='files/videos', null=True, verbose_name="")
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"'name':{self.name}, 'videofile':{self.videofile}, 'category':{self.category.name}"

class PriceOffers(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length=5000)

    def __str__(self):
        return f"'name':{self.name}, 'email':{self.email}, 'message':{self.message}"