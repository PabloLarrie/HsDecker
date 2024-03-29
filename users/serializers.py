from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Profile

UserModel = get_user_model()


class UserSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
        ]


class UserSerializer(UserSimpleSerializer):

    class Meta:
        model = UserModel
        fields = UserSimpleSerializer.Meta.fields + [
            "first_name",
            "last_name",
            "email",
            "is_superuser",
        ]


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
