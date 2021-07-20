from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_filters.backends import RestFrameworkFilterBackend

from users.filters import ProfilesFilter
from users.models import Profile
from users.serializers import ProfileSimpleSerializer, ProfileSerializer, UserSerializer


class UserViewSet(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(self.request.user).data, status=HTTP_200_OK)


class ProfileViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    filter_backends = (SearchFilter, RestFrameworkFilterBackend, OrderingFilter)
    search_fields = ["username"]
    filterset_class = ProfilesFilter
    ordering = ("id",)

    def get_serializer_class(self):
        if self.action == "list":
            return ProfileSimpleSerializer
        else:
            return ProfileSerializer
