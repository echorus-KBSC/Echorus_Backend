from django.contrib import admin
from django.urls import path

from .views import getAchievement, getSuccessCategory

urlpatterns = [
    path('',getAchievement),
    path('<int:category>',getSuccessCategory)
]