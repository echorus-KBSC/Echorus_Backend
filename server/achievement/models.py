from django.db import models

# Create your models here.
class Achievement(models.Model):
    id = models.AutoField(primary_key=True, blank=False,unique = True)
    name = models.CharField(null=False,max_length=100)
    success = models.IntegerField(null=False)
    description = models.TextField(null=False)
    count = models.IntegerField(null=0)
