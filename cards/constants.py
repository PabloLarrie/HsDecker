from django.db import models


class TypeCard(models.TextChoices):
    MINION = 'minion'
    SPELL = 'spell'
    WEAPON = 'weapon'
    HERO = 'hero'

class QualityCard(models.TextChoices):
    FREE = 'free'
    COMMON = 'common'
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'
