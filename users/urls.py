from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)


urlpatterns = [
    path('obtain/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
]
