from django.shortcuts import render
from rest_framework.response import Response
from .models import Card
from rest_framework.views import APIView
from .serializers import CardSerializer

class CardListAPI(APIView):
    def get(self,request):
        queryset = Card.objects.all()
        serializer = CardSerializer(queryset,many=True)
        return Response(serializer.data)
    def getCategory(self,category):
        queryset = Card.objects.get(pk=category)
        serializer = CardSerializer(queryset,many=True)
        return Response(serializer.data)
# Create your views here.
