from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

from .views import (
    RetriveUserCodeViewSet,
)


urlpatterns = [
    path('codes/<str:code>/', RetriveUserCodeViewSet.as_view()),
    path('obtain/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('verify/', verify_jwt_token),
]
