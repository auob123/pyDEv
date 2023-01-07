from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe




class feauters(models.Model):
    name = models.CharField(max_length=100)
    d1 = models.CharField(max_length=500)
    d2 = models.CharField(max_length=500, default='')
    d3 = models.CharField(max_length=500, default='')
    d4 = models.CharField(max_length=500, default='')
    d5 = models.CharField(max_length=500, default='')
    d6 = models.CharField(max_length=500, default='')
    d7 = models.CharField(max_length=500, default='')
    d8 = models.CharField(max_length=500, default='')
    d9 = models.CharField(max_length=500, default='')

class fields(models.Model):
    name = models.CharField(max_length=100)
    d1 = models.CharField(max_length=500)
    d2 = models.CharField(max_length=500, default='')
    d3 = models.CharField(max_length=500, default='')
    d4 = models.CharField(max_length=500, default='')
    d5 = models.CharField(max_length=500, default='')
    d6 = models.CharField(max_length=500, default='')
    d7 = models.CharField(max_length=500, default='')
    d8 = models.CharField(max_length=500, default='')
    d9 = models.CharField(max_length=500, default='')



class Востребованно(models.Model):
    for_images = models.ImageField(upload_to='images',default='')
    for_files = models.FileField(upload_to='files',default='')



class Географ(models.Model):
    images = models.ImageField(upload_to='img', default='')
    files = models.FileField(upload_to='file', default='')


class Навык(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)


class Послед(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

# Create your models here.
