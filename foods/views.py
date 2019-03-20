from django.shortcuts import render

from rest_framework import viewsets

from .models import (
    Food,
    FoodBackgroundImage,
)
from .serializers import (
    FoodSerializer,
    FoodBackgroundImageSerializer,
)


# Create your views here.

class FoodViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodBackgroundImageViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = FoodBackgroundImage.objects.all()
    serializer_class = FoodBackgroundImageSerializer