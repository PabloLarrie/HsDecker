from rest_framework_filters import FilterSet, filters

from cards.models import Card


class CardsFilter(FilterSet):
    hero = filters.CharFilter(field_name="hero", method="filter_hero")

    class Meta:
        model = Card
        fields = [
            "standard",
            "hero",
            "card_type",
            "quality",
            "race",
            "expansion",
            "cost",
            "keywords",
        ]  # filtrar id hero

    def filter_hero(self, qs, name, value):
        """
        QS -> Card.objects.filter(name="Prophet")
        name -> hero
        value -> id of the hero to search, for example 2
        """
        return qs.filter(heroes=value)
