from uo.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(read_only=True)
    #username = serializers.CharField(required=True, allow_blank=False, max_length=200)
    created = serializers.DateTimeField(read_only=True)
    password = serializers.CharField(required=True, allow_blank=False, max_length=200)
    class Meta:
        model = User
        fields = ("id", "username", "created", "password")
