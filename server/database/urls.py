from django.contrib import admin
from django.urls import path

from .views import get,getCategory, getId, getKeyword
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',get),
    path('category/<int:category>/',getCategory),
    path('<int:id>/',getId),
    path('search/',getKeyword)
]+static(settings.IMAGE_URL,document_root=settings.IMAGE_ROOT)