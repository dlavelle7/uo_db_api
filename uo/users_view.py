from uo.models import User
from uo.serializers import UserSerializer

from rest_framework import generics


class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class User(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
