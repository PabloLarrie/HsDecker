from django.contrib.auth import get_user_model
from rest_framework import serializers
from cards.models import Card, Expansion, HeroClass

UserModel = get_user_model()


class ExpansionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    id = serializers.IntegerField()

    class Meta:
        model = Expansion
        fields = [
            "id",
            "name",
        ]


class HeroClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    id = serializers.IntegerField()

    class Meta:
        model = HeroClass
        fields = [
            "id",
            "name",
        ]


class CardSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    heroes = serializers.SerializerMethodField()
    expansion = serializers.SerializerMethodField()

    def get_heroes(self, object):
        hero_list = []
        for hero in object.heroes.all():
            hero_list.append(hero.name)
        return hero_list

    def get_expansion(self, object):
        expansion_list = []
        for expansion in Expansion.objects.filter(id=object.expansion.id):
            expansion_list.append(expansion.name)
        return expansion_list

    class Meta:
        model = Card
        fields = [
            "id",
            "name",
            "card_type",
            "quality",
            "card_type",
            "heroes",
            "standard",
            "race",
            "expansion",
        ]
        read_only_fields = [
            "name",
            "card_type",
            "quality",
        ]


class CardSerializer(serializers.ModelSerializer):
    expansion = ExpansionSerializer()
    collection = serializers.CharField(
        source="expansion.collection.name", read_only=True
    )
    heroes = serializers.SerializerMethodField()
    usage = serializers.SerializerMethodField()

    def get_heroes(self, object):
        hero_list = []
        for hero in object.heroes.all():
            hero_list.append(hero.name)
        return hero_list

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
            "heroes",
            "endurance",
            "expansion",
            "collection",
            "usage",
        ]

        read_only_fields = [
            "id",
            "usage",
            "collection",
            "heroes",
        ]
