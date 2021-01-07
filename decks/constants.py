from django.db import models


class CardQuantityInDeck(models.IntegerChoices):
    ONE = 1
    TWO = 2
    