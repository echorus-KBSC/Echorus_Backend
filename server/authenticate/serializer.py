from rest_framework import serializers
from .models import AuthUser
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuthUser
        fields='__all__'
    def create(self,validated_data):
        login_id=validated_data.get('login_id')
        name=validated_data.get('name')
        password=validated_data.get('password')
        user = AuthUser(
            login_id=login_id,
            name=name
        )
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuthUser
        fields='__all__'