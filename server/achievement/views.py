from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AchievementSerializer
from .models import Achievement
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def getAchievement(self):
    queryset = Achievement.objects.all()
    serializer = AchievementSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSuccessCategory(self,category):
    queryset = Achievement.objects.filter(success=category)
    serializer = AchievementSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAchievementById(self,id):
    try:
        queryset=Achievement.objects.get(id=id)
    except:
        queryset = None
    if queryset is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        serializer=AchievementSerializer(queryset)
        return Response(serializer.data)