from rest_framework.response import Response
from .models import Card
from .serializers import CardSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get(self):
    queryset = Card.objects.all()
    serializer = CardSerializer(queryset,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getCategory(self,category):
    queryset=Card.objects.filter(category=category)
    serializer = CardSerializer(queryset,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getId(self,id):
    queryset=Card.objects.get(id=id)
    serializer = CardSerializer(queryset)
    return Response(serializer.data)
# Create your views here.
