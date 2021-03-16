from rest_framework_filters import FilterSet
from cards.models import Card, HeroClass


# class HeroFilter(CardsFilter):
#     class Meta:
#         model = HeroClass
#         fields = [
#             "id",
#             "name",
#         ]


class CardsFilter(FilterSet):
    # heroes = HeroFilter()

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
