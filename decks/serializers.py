from rest_framework import serializers
from decks.models import Deck, DeckCard
from cards.serializers import CardSerializer
from django.db.models import Sum


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
    complete = serializers.SerializerMethodField()
    cards = serializers.SerializerMethodField()
    total_cards = serializers.SerializerMethodField()

    def get_total_cards(self, object):
        return DeckCard.objects.filter(deck_id=object.id).aggregate(
            total=Sum("quantity")
        )["total"]

    def get_cards(self, object):
        return DeckCardSerializer(
            DeckCard.objects.filter(deck_id=object.id), many=True
        ).data

    def get_complete(self, object):
        return object.complete()

    class Meta:
        model = Deck
        fields = [
            "id",
            "name",
            "size",
            "hero_class",
            "standard",
            "cards",
            "complete",
            "size",
            "total_cards",
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