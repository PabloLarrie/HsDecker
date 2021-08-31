from rest_framework import serializers

from cards.models import HeroClass
from decks.models import Deck, DeckCard
from cards.serializers import CardSerializer, CardSimpleSerializer
from django.db.models import Sum

from users.serializers import UserSerializer, UserSimpleSerializer


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
    user = UserSimpleSerializer()

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
            "user",
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
    cards = DeckCardCreateSerializer(write_only=True, many=True, required=False)
    user = UserSerializer(read_only=True)
    hero_class = serializers.IntegerField()

    def create(self, validated_data):
        validated_data["hero_class"] = HeroClass.objects.get(id=validated_data["hero_class"])
        cards_data = validated_data.pop("cards", [])
        new_deck = Deck.objects.create(user=self.context['request'].user, **validated_data)
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
            "user",
            "hero_class",
        ]
