from this import d
from rest_framework import serializers
from .models import AchievementList, User

class userSerializer(serializers.ModelSerializer):  
    class Meta():
        model=User
        fields = '__all__'
        
class achievementListSerializer(serializers.ModelSerializer):
    class Meta():
        model=AchievementList
        fields=("user_id","id","achievement_id")
