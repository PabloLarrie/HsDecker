from rest_framework.viewsets import ModelViewSet
from cards.models import Card
from cards.serializers import CardSerializer, CardSimpleSerializer

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CardSimpleSerializer
        else: 
            return CardSerializer




