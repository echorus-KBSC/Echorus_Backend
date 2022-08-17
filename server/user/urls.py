from django.contrib import admin
from django.urls import path

from .views import getUserInfo,getUserInfoByName, saveUserAchievement,saveUserInfo

urlpatterns = [
    path('search',getUserInfo),
    path('search/<str:username>',getUserInfoByName),
    path('save',saveUserInfo),
    path('achievement',saveUserAchievement)
]