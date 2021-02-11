from rest_framework import serializers
from cards.models import Card, Expansion

class ExpansionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

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
