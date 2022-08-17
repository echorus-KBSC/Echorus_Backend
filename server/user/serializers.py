from this import d
from rest_framework import serializers
from .models import AcheievmentList, User

class userSerializer(serializers.ModelSerializer):  
    class Meta():
        model=User
        fields = '__all__'
        
class achievementListSerializer(serializers.ModelSerializer):
    class Meta():
        model=AcheievmentList
        fields=("user_id","id","achievement_id")
