from django.contrib import admin
from django.urls import path

from .views import helloAPI,get,getCategory

urlpatterns = [
    path('hello/',helloAPI),
    path('',get),
    path('<int:category>/',getCategory)
]