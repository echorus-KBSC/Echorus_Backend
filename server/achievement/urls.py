from django.contrib import admin
from django.urls import path

from .views import getAchievement, getAchievementById, getSuccessCategory

urlpatterns = [
    path('',getAchievement),
    path('category/<int:category>',getSuccessCategory),
    path('<int:id>',getAchievementById)
]