from rest_framework import serializers
from decks.models import Deck, DeckCard
from cards.serializers import CardSerializer, CardSimpleSerializer
from django.db.models import Sum


class DeckCardSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(read_only=True)
    golden = serializers.BooleanField(read_only=True)
    card = CardSerializer(read_only=True)

    class Meta:
        model = DeckCard
        fields = [
            "quantity",
            "golden",
            "card",
        ]


class DeckCardCreateSerializer(serializers.ModelSerializer):
    card = CardSimpleSerializer()

    class Meta:
        model = DeckCard
        fields = [
            "quantity",
            "golden",
            "card",
        ]


class DeckSimpleSerializer(serializers.ModelSerializer):
    hero_class = serializers.CharField(source="hero_class.name", read_only=True)
    complete = serializers.SerializerMethodField()
    total_cards = serializers.SerializerMethodField()

    def get_total_cards(self, object):
        return DeckCard.objects.filter(deck_id=object.id).aggregate(
            total=Sum("quantity")
        )["total"]

    def get_complete(self, object):
        return object.complete()

    class Meta:
        model = Deck
        fields = [
            "id",
            "name",
            "hero_class",
            "standard",
            "complete",
            "size",
            "total_cards",
        ]


class DeckSerializer(DeckSimpleSerializer):
    cards = serializers.SerializerMethodField()

    def get_cards(self, object):
        return DeckCardSerializer(
            DeckCard.objects.filter(deck_id=object.id), many=True
        ).data

    class Meta(DeckSimpleSerializer.Meta):
        fields = DeckSimpleSerializer.Meta.fields + [
            "cards",
        ]


class DeckCreateSerializer(DeckSimpleSerializer):
    cards = DeckCardCreateSerializer(write_only=True, many=True)

    def create(self, validated_data):
        cards_data = validated_data.pop("cards", [])
        new_deck = super().create(validated_data)
        for v in cards_data:
            DeckCard.objects.create(
                deck=new_deck,
                card_id=v["card"]["id"],
                quantity=v["quantity"],
                golden=v["golden"],
            )
        return new_deck

    class Meta(DeckSimpleSerializer.Meta):
        fields = DeckSimpleSerializer.Meta.fields + [
            "cards",
        ]
