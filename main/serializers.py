from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Region, Carservice, Masters


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'



class CarserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carservice
        
        fields = "__all__"


class MastersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masters
        
        fields = "__all__"




