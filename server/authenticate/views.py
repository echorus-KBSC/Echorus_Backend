from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate,get_user_model
# Create your views here.

AuthUser=get_user_model()
@api_view(['POST'])
def registerUser(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        token=TokenObtainPairSerializer.get_token(user)
        refresh_token=str(token)
        access_token=str(token.access_token)
        res = Response(
            {
                "user":serializer.data,
                "message":"register success",
                "token":{
                    "access":access_token,
                    "refresh":refresh_token,
                },
            },
            status=status.HTTP_200_OK,
        )
        res.set_cookie("access",access_token,httponly=True)
        res.set_cookie("refresh",refresh_token,httponly=True)
        return res
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
    id=request.data.get('login_id')
    password=request.data.get('password')
    user=authenticate(
        login_id=id,password=password
    )
    if user is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer=UserSerializer(user)
        token=TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token=str(token.access_token)
        res = Response(
            {
                "user":serializer.data,
                "message":"login success",
                "token":{
                    "access":access_token,
                    "refresh":refresh_token,
                },
            },
            status=status.HTTP_200_OK,
        )
        return res
@api_view(['POST'])
def logout(request):
    response = Response({
            "message": "Logout success"
            }, status=status.HTTP_202_ACCEPTED)
    response.delete_cookie('refresh')
    return response
