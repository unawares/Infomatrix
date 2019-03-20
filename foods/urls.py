from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from .views import (
    FoodViewSet,
    FoodBackgroundImageViewSet,
)


urlpatterns = [
]


router = routers.SimpleRouter()
router.register(r'background-images', FoodBackgroundImageViewSet, 'food-background-images')
router.register(r'', FoodViewSet, 'foods')
urlpatterns += router.urls
