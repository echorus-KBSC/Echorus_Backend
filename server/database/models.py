from distutils.command.upload import upload
from django.db import models

class Card(models.Model):
    id = models.AutoField(primary_key=True,blank=False,unique=True)
    image = models.ImageField(default='./image/default_image.jpg')
    title = models.CharField(max_length=100)
    category = models.IntegerField(null=False)
    style=models.IntegerField(null=False)
    description = models.TextField(null=False)
    soil = models.IntegerField(null=0)
    air = models.IntegerField(null=0)
    radio = models.IntegerField(null=0)
    trash=models.IntegerField(null=0)
    ocean = models.IntegerField(null=0)
    approval = models.IntegerField(null=0)
    capital = models.IntegerField(null=0)
    product = models.IntegerField(null=0)
# Create your models here.
