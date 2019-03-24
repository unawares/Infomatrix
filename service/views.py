from django.shortcuts import render

from rest_framework import status, viewsets

from .models import (
    FoodService,
    FoodServiceOrder,
)

from .serializers import (
    FoodServiceSerializer,
    FoodServiceOrderSerializer,
)


# Create your views here.

class FoodServiceViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = FoodService.objects.all()
    serializer_class = FoodServiceSerializer

