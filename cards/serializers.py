from rest_framework import serializers
from cards.models import Card, Expansion

class ExpansionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    id = serializers.IntegerField()

    class Meta:
        model = Expansion 
        fields = [
            "id",
            "name",
        ]

class CardSerializer(serializers.ModelSerializer):
    expansion = ExpansionSerializer()
    collection = serializers.CharField(source="expansion.collection.name", read_only=True)
    usage = serializers.SerializerMethodField()

    def get_usage(self, object):
        return object.usage()

    def create(self, validated_data):
        expansion_id = validated_data["expansion"]["id"]
        expansion = Expansion.objects.get(id=expansion_id)
        
        del validated_data["expansion"]
        card = Card.objects.create(**validated_data, expansion=expansion)
        return card

    class Meta:
        model = Card
        fields = [
            "id",
            "name",
            "description",
            "card_type",
            "quality",
            "race",
            "cost",
            "attack",
            "endurance",
            "expansion",
            "collection",
            "usage",
        ]
