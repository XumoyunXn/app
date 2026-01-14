from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Region, Carservice, Masters, Country, New
from .serializers import RegionSerializer, CarserviceSerializer, MastersSerializer, CountrySerializer, NewSerializer
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly

class CountryList(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

    def get_queryset(self):
        return Country.objects.all()
    
    def get(self, request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)


class NewList(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

    def get_queryset(self):
        return New.objects.all()
    
    def get(self, request):
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data)



class RegionList(generics.ListAPIView): 
    serializer_class = RegionSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        country_id = self.kwargs["id"]
        return Region.objects.filter(country_id=country_id)





class Carservices(generics.ListAPIView):
    serializer_class = CarserviceSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        region_id = self.kwargs["id"]
        return Carservice.objects.filter(region_id=region_id)


class MastersList(generics.ListAPIView):
    serializer_class = MastersSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        carservice_id = self.kwargs["id"]
        return Masters.objects.filter(carservice_id=carservice_id)

