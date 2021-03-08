from rest_framework.viewsets import ModelViewSet
from cards.models import Card
from cards.serializers import CardSerializer, CardSimpleSerializer
from rest_framework.filters import SearchFilter
from cards.filters import CardsFilter
from rest_framework_filters.backends import RestFrameworkFilterBackend


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    filter_backedns = (SearchFilter, RestFrameworkFilterBackend)
    search_fields = ["name", "keywords_name", "card_type", "quality"]
    filterset_class = CardsFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CardSimpleSerializer
        else:
            return CardSerializer
