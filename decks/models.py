from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=50, unique=True)
    size = models.PositiveIntegerField()
    cards = models.ManyToManyField('cards.Card', through='DeckCard')

class CardQuantityInDeck(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3



class DeckCard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.ForeignKey('cards.Card', on_delete=models.CASCADE)
    quantity = models.IntegerField(choices=CardQuantityInDeck.choices)
    golden = models.BooleanField()