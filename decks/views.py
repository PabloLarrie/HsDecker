from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from decks.models import Deck
from decks.serializers import DeckSerializer, DeckSimpleSerializer, DeckCreateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from decks.filters import DecksFilter
from rest_framework_filters.backends import RestFrameworkFilterBackend


class DeckViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Deck.objects.all()
    filter_backends = (SearchFilter, RestFrameworkFilterBackend)
    search_fields = ["name", "hero_class", "standard"]
    filterset_class = DecksFilter
    ordering = ("id",)

    def get_serializer_class(self):
        if self.action == "list":
            return DeckSimpleSerializer
        if self.action == "create":
            return DeckCreateSerializer
        else:
            return DeckSerializer
