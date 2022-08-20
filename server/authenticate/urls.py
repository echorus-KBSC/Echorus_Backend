from atexit import register
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import logout, registerUser,login

urlpatterns = [
    path('register',registerUser),
    path('login',login),
    path('login/refresh',TokenRefreshView.as_view()),
    path('logout',logout)
]