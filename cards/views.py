from rest_framework.viewsets import ModelViewSet
from cards.models import Card
from cards.serializers import CardSerializer, CardSimpleSerializer

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardSimpleViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSimpleSerializer