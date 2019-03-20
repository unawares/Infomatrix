from rest_framework import serializers

from .models import (
    Food,
    FoodBackgroundImage,
)


class FoodBackgroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodBackgroundImage
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):

    food_background_image = FoodBackgroundImageSerializer(read_only=True)

    class Meta:
        model = Food
        fields = '__all__'
