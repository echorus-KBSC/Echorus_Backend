from typing import List
from django.db import models

class User(models.Model):
    id=models.AutoField(null=False,primary_key=True)
    username=models.CharField(null=False,max_length=20)
    soil = models.IntegerField(null=0)
    air = models.IntegerField(null=0)
    radio = models.IntegerField(null=0)
    trash=models.IntegerField(null=0)
    ocean = models.IntegerField(null=0)
    approval = models.IntegerField(null=0)
    capital = models.IntegerField(null=0)
    product = models.IntegerField(null=0)
    year=models.IntegerField(null=2020)
    success = models.IntegerField(null=0) # 0:성공 1:실패 2:진행중
    
class AcheievmentList(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey('User',on_delete=models.CASCADE)
    username=models.CharField(null=False,max_length=20)
    achievement_id=models.IntegerField(null=False)
# Create your models here.

class UserData:
    def __init__(self,User,array):
        self.User = User
        self.AchievementArray = array