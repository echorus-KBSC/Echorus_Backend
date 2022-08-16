from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import userSerializer

from .models import User

# Create your views here.
@api_view(['GET']) # /user
def getUserInfo(self,request):
    queryset = User.objects.all()
    serializer = userSerializer(queryset,many=True)
    return Response(serializer.data)
@api_view(['GET']) # /user/name 업적도 들고와야함
def getUserInfoByName(self,request,name):
    queryset = User.objects.get(username=name)
    serializer=userSerializer(queryset)
    return Response(serializer.data)
@api_view(['POST']) #/user/save
def saveUserInfo(self,request):
    user_info=userSerializer(data=request.data)
    name = request.GET.get('username')
    user,created=User.objects.get_or_create(username=name)
    if created:
        if user_info.is_valid():
            user_info.save()
            return Response(user_info.data)
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        if user_info.is_valid():
            user_info.save()
            return Response(user_info.data)
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def completeUserInfo(self,request): #user/complete
    user_info=userSerializer(data=request.data)
    name = request.GET.get('username')
    user,created=User.objects.get_or_create(username=name)
    if created:
        if user_info.is_valid():
            user_info.save()
            return Response(user_info.data)
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
        


