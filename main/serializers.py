from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Region, Carservice, Masters, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


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




