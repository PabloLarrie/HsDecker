from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Profile

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "username",
            "user",
            "email",
            "bio",
            "avatar",
        )


class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "username",
            "user",
        )
