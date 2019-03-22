from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins

from .models import (
    UserCode,
)

from .serializers import (
    UserCodeSerializer,
)

# Create your views here.

class RetriveUserCodeViewSet(generics.RetrieveAPIView):
    
    lookup_field = 'code'
    serializer_class = UserCodeSerializer
    queryset = UserCode.objects.all()