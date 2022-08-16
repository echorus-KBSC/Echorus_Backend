from django.contrib import admin
from django.urls import path

from .views import getUserInfo,getUserInfoByName,saveUserInfo,completeUserInfo

urlpatterns = [
    path('',getUserInfo),
    path('<str:username>/',getUserInfoByName),
    path('save/',saveUserInfo),
    path('complete/',completeUserInfo)
]