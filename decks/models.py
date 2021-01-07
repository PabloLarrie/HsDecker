from django.db import models
from decks.constants import CardQuantityInDeck


class Deck(models.Model):
    name = models.CharField(max_length=50, unique=True)
    size = models.PositiveIntegerField()
    cards = models.ManyToManyField('cards.Card', through='DeckCard')


class DeckCard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card = models.ForeignKey('cards.Card', on_delete=models.CASCADE)
    quantity = models.IntegerField(choices=CardQuantityInDeck.choices)
    golden = models.BooleanField()
