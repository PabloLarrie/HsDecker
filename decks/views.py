from rest_framework.viewsets import ModelViewSet
from decks.models import Deck
from decks.serializers import DeckSerializer, DeckSimpleSerializer

class DeckViewSet(ModelViewSet):
    queryset = Deck.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return DeckSimpleSerializer
        else: 
            return DeckSerializer