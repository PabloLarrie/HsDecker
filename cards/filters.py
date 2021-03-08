from rest_framework_filters import FilterSet
from cards.models import Card


class CardsFilter(FilterSet):
    class Meta:
        model = Card
        fields = ["standard"]  # filtrar id hero
