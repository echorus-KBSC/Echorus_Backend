from rest_framework.response import Response
from .models import Card
from .serializers import CardSerializer
from rest_framework.decorators import api_view
from django.db.models import Q

@api_view(['GET'])
def get(self):
    result = {}
    queryset = Card.objects.all()
    serializer = CardSerializer(queryset,many=True)
    result['Cards']=serializer.data
    return Response(result)
@api_view(['GET'])
def getCategory(self,category):
    result = {}
    try:
        queryset=Card.objects.filter(category=category)
    except Card.DoesNotExist:
        queryset= None
    if queryset is None:
        return []
    else:
        serializer = CardSerializer(queryset,many=True)
        result['Cards']=serializer.data
        return Response(result)
@api_view(['GET'])
def getId(self,id):
    queryset=Card.objects.get(id=id)
    serializer = CardSerializer(queryset)
    return Response(serializer.data)
@api_view(['GET'])
def getKeyword(request):
    result = {}
    keyword = request.GET.get('word',None)
    option = request.GET.get('opt',None)
    if option == '0':
        queryset=Card.objects.filter(title__contains=keyword)
    elif option == '1':
        queryset=Card.objects.filter(description__contains=keyword)
    else:
        queryset=Card.objects.filter(Q(title__contains=keyword) | Q(description__contains=keyword))
    serializer = CardSerializer(queryset,many=True)
    result['Cards']=serializer.data
    return Response(result)
