from django.contrib import admin
from django.urls import path

from .views import get,getCategory
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',get),
    path('<int:category>/',getCategory)
]+static(settings.IMAGE_URL,document_root=settings.IMAGE_ROOT)