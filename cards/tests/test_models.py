import pytest
from decks.models import DeckCard


pytestmark = pytest.mark.django_db
class TestCards:

    def test_usage(self, deck_warrior, deck_priest, card_neutral, card_legendary, card_priest):
        DeckCard(deck=deck_warrior, card=card_legendary, quantity=1, golden=False).save()
        DeckCard(deck=deck_warrior, card=card_neutral, quantity=1, golden=True).save()        
        DeckCard(deck=deck_priest, card=card_neutral, quantity=1, golden=False).save()
        DeckCard(deck=deck_priest, card=card_neutral, quantity=1, golden=True).save()
        assert card_legendary.usage() == 50
        assert card_neutral.usage() == 100
        assert card_priest.usage() == 0
    