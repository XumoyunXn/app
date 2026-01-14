# users/urls.py
from django.urls import path
from .views import RegionList, Carservices, MastersList, CountryList, NewList

urlpatterns = [
    path("country/", CountryList.as_view(), name="country"),
    path('region/<int:id>/', RegionList.as_view(), name="region"),
    path("carservices/<int:id>/", Carservices.as_view(), name="carservices"),
    path("masters/<int:id>/", MastersList.as_view(), name="masters"),
    path("news/", NewList.as_view(), name="new")

]
