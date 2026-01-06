# users/urls.py
from django.urls import path
from .views import RegionList, Carservices, MastersList

urlpatterns = [
    path('region/', RegionList.as_view(), name="region"),
    path("carservices/<int:id>/", Carservices.as_view()),
    path("masters/<int:id>/", MastersList.as_view()),

]
