from rest_framework import serializers
from decks.models import Deck, DeckCard


class DeckCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeckCard
        fields = [
        "id",
        "deck_id",
        "card_id",
        "quantity",
        "golden",
        ]


class DeckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deck
        fields = [
            "id",
            "name",
            "size",
            "cards",
            "hero_class",
            "standard",
        ]
        