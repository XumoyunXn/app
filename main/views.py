from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Region, Carservice, Masters
from .serializers import RegionSerializer, CarserviceSerializer, MastersSerializer
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly





class RegionList(APIView): 
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

    def get_queryset(self):
        return Region.objects.all()
    
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)


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