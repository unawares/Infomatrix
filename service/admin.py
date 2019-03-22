from django.contrib import admin

from .models import (
    FoodService,
    FoodServiceOrder,
)

# Register your models here.

admin.site.register(FoodService)
admin.site.register(FoodServiceOrder)