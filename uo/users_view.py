from uo.models import User
from uo.serializers import UserSerializer
from uo.permissions import UsersAccessPermission

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response


class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UsersAccessPermission,)

    def post(self, request):
        if User.objects.filter(username=request.data["username"]).exists():
            return Response({"error": "Username already taken."},
                            status=status.HTTP_409_CONFLICT)
        return super().post(request)


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
