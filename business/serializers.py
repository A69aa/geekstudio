from rest_framework import serializers
from .models import CustomUser,GeektechDirections
from django.contrib.auth.hashers import make_password


class UsersListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}



    def create(self, validated_data):
        _user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password = make_password(validated_data['password']))



class GeekDirectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeektechDirections
        fields = '__all__'