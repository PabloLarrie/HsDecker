from django.db import models
from cards.constants import TypeCard


class Card(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cost = models.PositiveIntegerField() 
    expansion = models.ForeignKey('cards.Expansion', related_name="cards", on_delete=models.CASCADE)
    heros = models.ManyToManyField('cards.HeroClass')
    decks = models.ManyToManyField('decks.Deck', through='decks.DeckCard')
    card_type = models.CharField(max_length=6, default=TypeCard.MINION, choices=TypeCard.choices) 
    keywords = models.ManyToManyField('cards.KeyWord', related_name="cards")
    attack = models.PositiveIntegerField(null=True)
    endurance = models.PositiveIntegerField(null=True)


class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    year = models.DateTimeField()
    

class Expansion(models.Model):
    name = models.CharField(max_length=50, unique=True)
    collection = models.ForeignKey(Collection, related_name="expansions", on_delete=models.CASCADE)


class Power(models.Model):
    name = models.CharField(max_length=15, unique=True)
    cost = models.IntegerField()
    description = models.TextField(max_length=200)


class HeroClass(models.Model):
    name = models.CharField(max_length=15, unique=True)
    power = models.ForeignKey(Power, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)


class Hero(models.Model):
    name = models.CharField(max_length=15, unique=True)
    hero_class = models.ForeignKey(HeroClass, related_name="heroes", on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    health = models.PositiveIntegerField(default=30)
    armor = models.PositiveIntegerField(default=0)


class KeyWord(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200)
     
 
