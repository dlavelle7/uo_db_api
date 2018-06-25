from uo.models import User
from uo.serializers import UserSerializer
from uo.permissions import UsersAccessPermission

from rest_framework import generics
from rest_framework.response import Response


class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UsersAccessPermission,)

    def post(self, request):
        return super().post(request)


class User(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
