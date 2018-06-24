from uo.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False,
                                     max_length=200)
    # FIXME: Password and token should not be here
    password = serializers.CharField(required=True, allow_blank=False,
                                     max_length=200)
    auth_token = serializers.SlugRelatedField(read_only=True, slug_field='key')

    def create(self, validated_data):
        """Override create() for django.contrib.auth.User create_user()."""
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ("id", "username", "password", "auth_token")
