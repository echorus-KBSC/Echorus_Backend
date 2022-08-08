from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AchievementSerializer
from .models import Achievement
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