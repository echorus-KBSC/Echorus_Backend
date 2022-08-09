
from django.contrib import admin
from django.urls import path

from .views import get,getCategory

urlpatterns = [
    path('',get),
    path('<int:category>/',getCategory)
]