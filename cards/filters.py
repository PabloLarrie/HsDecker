from rest_framework_filters import FilterSet
from cards.models import Card


class CardsFilter(FilterSet):
    class Meta:
        model = Card
        fields = [
            "standard",
            "heroes",
            "card_type",
            "quality",
            "race",
            "expansion",
            "cost",
            "keywords",
        ]  # filtrar id hero
