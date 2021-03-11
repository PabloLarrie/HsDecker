from rest_framework_filters import FilterSet
from decks.models import Deck


class DecksFilter(FilterSet):
    class Meta:
        model = Deck
        fields = [
            "hero_class",
            "standard",
        ]  # filtrar id hero
