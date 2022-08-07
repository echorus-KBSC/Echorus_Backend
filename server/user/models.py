from django.db import models

class User(models.Model):
    id=models.AutoField(null=False,primary_key=True)
    userId=models.CharField(null=False,primary_key=True,max_length=20)
    name=models.CharField(null=False,max_length=10)
    password=models.CharField(null=False,max_length=15)
    
# Create your models here.
