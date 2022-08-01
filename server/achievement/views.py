from django.shortcuts import render
from httplib2 import Response
from rest_framework.decorators import api_view

from achievement.serializers import AchievementSerializer
from .models import Achievement
# Create your views here.

@api_view(['GET'])
def getAchievement(self):
    queryset = Achievement.objects.all()
    serializer = AchievementSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSuccessCategory(self,category):
    queryset = Achievement.objects.get(success=category)
    serializer = AchievementSerializer(queryset,many=True)
    return Response(serializer.data)