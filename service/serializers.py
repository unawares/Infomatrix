from rest_framework import serializers

from django.utils.translation import ugettext, ugettext_lazy as _

from .models import (
    FoodService,
    FoodServiceOrder,
)


class FoodServiceOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodServiceOrder
        fields = '__all__'
        read_only_fields = ('food_service',)


class FoodServiceSerializer(serializers.ModelSerializer):

    orders = FoodServiceOrderSerializer(many=True)

    class Meta:
        model = FoodService
        fields = '__all__'


class FoodServiceOrderActionSerializer(serializers.Serializer):

    SUBMIT = 'submit'
    CANCEL = 'cancel'
    
    ACTION = (
        (SUBMIT, _('Submit')),
        (CANCEL, _('Cancel'))
    ) 

    code = serializers.CharField()
    action = serializers.ChoiceField(choices=ACTION)