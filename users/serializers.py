from rest_framework import serializers

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
        )


class UserCodeSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserCode
        fields = '__all__'