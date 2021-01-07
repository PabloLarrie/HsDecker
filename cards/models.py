from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
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
     
class Card(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cost = models.PositiveIntegerField() 
    expansion = models.ForeignKey(Expansion, related_name="cards", on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, related_name="cards", on_delete=models.CASCADE)
    decks = models.ManyToManyField('decks.Deck', through='decks.DeckCard')
   
