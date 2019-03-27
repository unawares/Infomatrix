from rest_framework import serializers

from service.serializers import FoodServiceSerializer
from service.models import FoodService

from .models import (
    CustomUser,
    UserCode,
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'full_name',
        )


class UserCodeSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    services = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserCode
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'active',)

    def get_services(self, obj):
        return {
            'foods': FoodServiceSerializer(
                [service
                    for service in obj.user.services.all()
                        if type(service) is FoodService],
                many=True).data
        }