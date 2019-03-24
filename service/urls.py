from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import (
    FoodServiceViewSet,
)


urlpatterns = [

]

router = SimpleRouter()
router.register(r'foods', FoodServiceViewSet)

urlpatterns += router.urls