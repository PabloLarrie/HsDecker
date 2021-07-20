from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework_filters.backends import RestFrameworkFilterBackend

from cards.filters import CardsFilter
from cards.models import Card, Expansion, HeroClass
from cards.serializers import CardSerializer, CardSimpleSerializer, ExpansionSerializer, HeroClassSerializer


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


class HeroClassViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = HeroClass.objects.all()

    def get_serializer_class(self):
        return HeroClassSerializer
