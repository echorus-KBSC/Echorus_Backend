from django.db import models

# Create your models here.
class Achievement(models.Model):
    id = models.AutoField(primary_key=True, blank=False,unique = True)
    name = models.CharField(null=False,max_length=100)
    success = models.IntegerField(null=False)
    description = models.TextField(null=False)
    count = models.IntegerField(null=0)
    soil = models.IntegerField(null=0)
    air = models.IntegerField(null=0)
    radio = models.IntegerField(null=0)
    trash=models.IntegerField(null=0)
    ocean = models.IntegerField(null=0)
    approval = models.IntegerField(null=0)
    capital = models.IntegerField(null=0)
    product = models.IntegerField(null=0)
    disaster=models.IntegerField(null=0)
    universe=models.IntegerField(null=0)
    year=models.IntegerField(null=2000)

