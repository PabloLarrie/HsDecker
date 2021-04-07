from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from cards.models import Card
from cards.serializers import CardSerializer, CardSimpleSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from cards.filters import CardsFilter
from rest_framework_filters.backends import RestFrameworkFilterBackend


class CardViewSet(ModelViewSet):
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
