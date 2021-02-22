from rest_framework import serializers
from decks.models import Deck, DeckCard
from cards.serializers import CardSerializer


class DeckCardSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(read_only=True)
    golden = serializers.CharField(read_only=True)
    card = CardSerializer(read_only=True)

    class Meta:
        model = DeckCard
        fields = [
        "quantity",
        "golden",
        "card",
        ]

class DeckSerializer(serializers.ModelSerializer):
    hero_class = serializers.CharField(source="hero_class.name", read_only=True)
    cards = serializers.SerializerMethodField()

    def get_cards(self, object):
        return DeckCardSerializer(DeckCard.objects.filter(deck_id=object.id), many=True).data

    class Meta:
        model = Deck
        fields = [
            "id",
            "name",
            "size",
            "hero_class",
            "standard",
            "cards",
        ]
        


class DeckSimpleSerializer(serializers.ModelSerializer):
    hero_class = serializers.CharField(source="hero_class.name", read_only=True)

    class Meta:
        model = Deck
        fields = [
            "id",
            "name",
            "hero_class",
            "standard",
        ]