from django.db import models

from django.dispatch import receiver
from django.db.models.signals import pre_save

from django.contrib.auth.models import Group

from users.models import CustomUser
from foods.models import Food


# Utils


# Create your models here.

class Service(models.Model):

    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='services'
    )
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True


class FoodService(Service):

    food = models.ForeignKey(
        'foods.Food',
        on_delete=models.CASCADE,
        related_name='services'
    )
    amount = models.IntegerField(
        blank=False,
        null=False,
        default=1
    )

    class Meta:
        unique_together = ('client', 'food',)


class FoodServiceOrder(models.Model):

    food_service = models.ForeignKey(
        FoodService,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    created = models.DateTimeField(auto_now_add=True)


# Signals
@receiver(pre_save, sender=FoodServiceOrder)
def food_service_item_pre_save_handler(sender, instance, *args, **kwargs):
    if not instance.food_service.active:
        raise Exception('Can not make an order. Food service is not activated')
    if instance.food_service.food_service_orders.count() >= instance.food_service.amount:
        raise Exception('Can not make an order. Number of max allowed orders is reached')
