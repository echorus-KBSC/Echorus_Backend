from re import A
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import achievementListSerializer, userSerializer

from .models import AcheievmentList, User, UserData

# Create your views here.
@api_view(['GET']) # /user
def getUserInfo(self):
    queryset = User.objects.all()
    serializer = userSerializer(queryset,many=True)
    return Response(serializer.data)
@api_view(['GET']) # /user/name 업적도 들고와야함
def getUserInfoByName(self,username):
    try:
        queryset = User.objects.get(username=username)
    except:
        queryset=None
    if queryset is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        serializer=userSerializer(queryset)
        try:
            achieveQueryset = AcheievmentList.objects.filter(id=serializer.data['id'])
        except AcheievmentList.DoesNotExist:
            achieveQueryset=None
        if achieveQueryset is None:
            userData = UserData(serializer.data,[])
        else:
            userDataSerializer = achievementListSerializer(achieveQueryset,many=True)
            userData = UserData(serializer.data,list(userDataSerializer.data))
        return Response(userData)
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
def completeUserInfo(self,request,username): #user/complete
    user_info=userSerializer(data=request.data)
    user,created=User.objects.get_or_create(username=user_info.data['username'])
    if created:
        if user_info.is_valid():
            user_info.save()
            return Response(user_info.data)
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
        


