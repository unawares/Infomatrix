from rest_framework import serializers

from .models import (
    FoodService,
    FoodServiceOrder,
)


class FoodServiceOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodServiceOrder
        fields = '__all__'


class FoodServiceSerializer(serializers.ModelSerializer):

    orders = FoodServiceOrderSerializer(many=True)

    class Meta:
        model = FoodService
        fields = '__all__'
