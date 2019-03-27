from pprint import pprint
from datetime import datetime, timedelta

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied

from users.models import (
    UserCode,
)

from users.serializers import (
    UserCodeSerializer,
)

from .models import (
    FoodService,
    FoodServiceOrder,
)

from .serializers import (
    FoodServiceSerializer,
    FoodServiceOrderSerializer,
    FoodServiceOrderActionSerializer,
)


# Create your views here.

class FoodServiceViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = FoodService.objects.all()
    serializer_class = FoodServiceSerializer

    @action(detail=True, methods=['post'], serializer_class=FoodServiceOrderActionSerializer, url_path='orders')
    def make_order(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_code = get_object_or_404(UserCode, code=serializer.data['code'])
        food_service = get_object_or_404(FoodService, pk=pk, client=user_code.user)
        if serializer.data['action'] == self.get_serializer_class().SUBMIT:
            order = FoodServiceOrder.objects.create(food_service=food_service)
        elif serializer.data['action'] == self.get_serializer_class().CANCEL:
            end = datetime.now()
            start = end - timedelta(minutes=5)
            try:
                order = food_service.orders.filter(created__range=[start, end]).latest('created').delete()
            except FoodServiceOrder.DoesNotExist:
                raise PermissionDenied()
        return Response(serializer.data)