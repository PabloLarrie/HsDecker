from django.db import models


class TypeCard(models.TextChoices):
    MINION = 'Minion'
    SPELL = 'Spell'
    WEAPON = 'Weapon'
    HERO = 'Hero'
