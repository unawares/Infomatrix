from django.contrib import admin

from .models import (
    Food,
    FoodBackgroundImage,
)

# Register your models here.

admin.site.register(Food)
admin.site.register(FoodBackgroundImage)