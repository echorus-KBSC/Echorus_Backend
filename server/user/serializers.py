from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    userId=serializers.CharField(
        required=True,
        write_only=True,
        max_length=15,
    )
    password=serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type':'password'}
    )
    name=serializers.CharField(
        required=True,
        write_only=True,
        max_length=20
    )
    class Meta():
        model=User
        field = '__all__'
    
