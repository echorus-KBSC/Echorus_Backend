import json
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
        return Response([])
    else:
        serializer=userSerializer(queryset)
        try:
            achieveQueryset = AcheievmentList.objects.filter(user_id_id=serializer.data['id'])
        except AcheievmentList.DoesNotExist:
            achieveQueryset=None
        if achieveQueryset is None:
            userData = UserData(serializer.data,[])
        else:
            userDataSerializer = achievementListSerializer(achieveQueryset,many=True)
            userData = UserData(serializer.data,list(userDataSerializer.data))
        return Response(userData.__dict__)
@api_view(['POST']) #/user/save
def saveUserInfo(request):
    user_info=userSerializer(data=request.data)
    if user_info.is_valid():
        name = user_info.validated_data.get('username')
        try:
            user=User.objects.get(username=name)
        except:
            user = None
        if user is None:
            user_info.save()
            return Response(user_info.data)
        else:
            update_user = userSerializer(user,data=request.data)
            if update_user.is_valid():
                update_user.save()
                return Response(update_user.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def saveUserAchievement(request):
    username=request.data['username']
    try:
        queryset = User.objects.get(username=username)
    except:
        queryset=None
    if queryset is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        request.data['user_id']=queryset.id
        print(request.data)
        achieveSerializer=achievementListSerializer(data=request.data)
        if achieveSerializer.is_valid():
            achieveSerializer.save()
            return Response(achieveSerializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

            


