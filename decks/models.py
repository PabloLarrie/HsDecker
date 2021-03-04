from django.db import models
from cards.constants import QualityCard
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum, CheckConstraint, Q, F


class Deck(models.Model):
    name = models.CharField(max_length=50)
    size = models.PositiveIntegerField(default=30)
    hero_class = models.ForeignKey(
        "cards.HeroClass", related_name="decks", on_delete=models.CASCADE,  null=True
    )
    cards = models.ManyToManyField("cards.Card", through="DeckCard")

    standard = models.BooleanField(default=True)

    def complete(self):
        return (
            self.size
            == DeckCard.objects.filter(deck_id=self.id).aggregate(
                total=Sum("quantity")
            )["total"]
        )


class DeckCard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="deck_cards")
    card = models.ForeignKey(
        "cards.Card", on_delete=models.CASCADE, related_name="deck_cards"
    )

    quantity = models.IntegerField(
        validators=[MaxValueValidator(2), MinValueValidator(1)]
    )
    golden = models.BooleanField()

    class Meta:
        unique_together = (("deck", "card", "golden"),)

    def save(self, *args, **kwargs):
        total = DeckCard.objects.filter(
            card_id=self.card.id, deck_id=self.deck.id
        ).aggregate(total=Sum("quantity"))["total"]

        if total is None:
            total = 0
        total_copies = total + self.quantity
        if (
            self.card.quality != QualityCard.LEGENDARY
            and total_copies > 2
            or self.card.quality == QualityCard.LEGENDARY
            and total_copies > 1
        ):
            raise ValueError("Reached maximun allowed quantity for this card")
        if (
            self.card.heroes.all()
            and self.deck.hero_class not in self.card.heroes.all()
        ):
            raise ValueError(
                "A deck can only contain cards of the same class and neutrals"
            )
        if self.deck.standard and not self.card.standard:
            raise ValueError("This card does not belong to Standard Format")
        super().save(*args, **kwargs)
