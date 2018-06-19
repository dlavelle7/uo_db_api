from uo.models import User
from uo.serializers import UserSerializer
from uo.permissions import UsersAccessPermission

from rest_framework import generics
from rest_framework.decorators import permission_classes


class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UsersAccessPermission,)


class User(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
