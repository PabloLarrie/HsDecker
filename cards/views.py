from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from cards.models import Card, Expansion
from cards.serializers import CardSerializer, CardSimpleSerializer, ExpansionSerializer, UserSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from cards.filters import CardsFilter
from rest_framework_filters.backends import RestFrameworkFilterBackend


class CardViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Card.objects.all()
    filter_backends = (SearchFilter, RestFrameworkFilterBackend, OrderingFilter)
    search_fields = ["name", "keywords__name", "card_type", "quality"]
    filterset_class = CardsFilter
    ordering = ("id",)

    def get_serializer_class(self):
        if self.action == "list":
            return CardSimpleSerializer
        else:
            return CardSerializer


class ExpansionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Expansion.objects.all()
    filter_backends = (SearchFilter, RestFrameworkFilterBackend, OrderingFilter)
    search_fields = ["name", "collection"]
    ordering = ("id",)

    def get_serializer_class(self):
        return ExpansionSerializer


class UserViewSet(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(self.request.user).data, status=HTTP_200_OK)
