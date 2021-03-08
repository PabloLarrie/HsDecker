from rest_framework.viewsets import ModelViewSet
from decks.models import Deck
from decks.serializers import DeckSerializer, DeckSimpleSerializer
from rest_framework import filters


class DeckViewSet(ModelViewSet):
    queryset = Deck.objects.all()
    filter_decks = (filters.SearchFilter,)
    filter_fields = ["name", "hero_class", "standard"]

    def get_serializer_class(self):
        if self.action == "list":
            return DeckSimpleSerializer
        else:
            return DeckSerializer