from django.contrib.auth import authenticate
from rest_framework import generics,permissions
from .serializers import (
    UsersListSerializers,
    UsersDetailSerializer,
    UserCreateSerializer,
    GeekDirectionsSerializer,
)
from .models import CustomUser,GeektechDirections


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersListSerializers



class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.filter()
    serializer_class = UsersDetailSerializer
    lookup_field = 'id'



class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer



class GeektechDirectionsView(generics.ListAPIView):
    queryset = GeektechDirections.objects.all()
    serializer_class = GeekDirectionsSerializer
    permission_classes = [permissions.IsAuthenticated]