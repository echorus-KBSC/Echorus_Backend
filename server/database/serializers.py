import base64
from msilib.schema import File
from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
    def getImage(self,obj):
        try:
            f=open("image/"+obj.image,'rb')
            data = base64.b64decode(File(f).read())
            f.close()
            return data
        except IOError:
            print('IO error')
            return -1