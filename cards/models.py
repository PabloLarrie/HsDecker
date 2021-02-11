from django.db import models
from cards.constants import TypeCard, QualityCard
from decks.models import Deck


class Card(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300, null=True)
    heroes = models.ManyToManyField('cards.HeroClass', related_name="cards")
    card_type = models.CharField(max_length=6, default=TypeCard.MINION, choices=TypeCard.choices)
    quality = models.CharField(max_length=12, default=QualityCard.COMMON, choices=QualityCard.choices)
    race = models.CharField(max_length=12, null=True)
    expansion = models.ForeignKey('cards.Expansion', related_name="cards", on_delete=models.CASCADE)
    cost = models.IntegerField()
    attack = models.PositiveIntegerField(null=True) 
    endurance = models.PositiveIntegerField(null=True)
    collectible = models.BooleanField(default=False)
    keywords = models.ManyToManyField('cards.KeyWord', related_name="cards", blank=True) 
    decks = models.ManyToManyField('decks.Deck', through='decks.DeckCard', blank=True)

    def usage(self):
        n_decks = Deck.objects.count()
        n_usage = Deck.objects.filter(cards=self).distinct().count()
        if n_usage > 0:    
            return n_usage / n_decks * 100
        else:
            return 0
        

class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    year = models.PositiveIntegerField()
    

class Expansion(models.Model):
    name = models.CharField(max_length=50, unique=True)
    collection = models.ForeignKey(Collection, related_name="expansions", on_delete=models.CASCADE)


class Power(models.Model):
    name = models.CharField(max_length=15, unique=True)
    cost = models.IntegerField()
    description = models.TextField(max_length=200)


class HeroClass(models.Model):
    name = models.CharField(max_length=15, unique=True)
    power = models.ForeignKey(Power, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=200, null=True)


class Hero(models.Model):
    name = models.CharField(max_length=30, unique=True)
    hero_class = models.ForeignKey(HeroClass, related_name="heroes", on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    health = models.PositiveIntegerField(default=30)
    armor = models.PositiveIntegerField(default=0)


class KeyWord(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=450)