import pytest
from decks.models import DeckCard
from tests.conftest import class_warrior, class_priest, card_vellen, card_control, deck_warrior, card_inner, card_addict 

pytestmark = pytest.mark.django_db
class TestDecks:
    
    def test_legendary_uniqueness(self, class_warrior, card_vellen, deck_warrior):
        with pytest.raises(ValueError):
            DeckCard(deck=deck_warrior, card=card_vellen, quantity=2, golden=False).save()
        DeckCard(deck=deck_warrior, card=card_vellen, quantity=1, golden=False).save()
        with pytest.raises(ValueError):
            DeckCard(deck=deck_warrior, card=card_vellen, quantity=1, golden=False).save()
        

    def test_same_class(self, class_warrior, class_priest, card_control, card_inner, card_addict, deck_warrior):
        DeckCard(deck=deck_warrior, card=card_inner, quantity=2, golden=False).save()
        with pytest.raises(ValueError):
            DeckCard(deck=deck_warrior, card=card_control, quantity=2, golden=False).save()

        DeckCard(deck=deck_warrior, card=card_addict, quantity=2, golden=False).save()

        assert card_addict in deck_warrior.cards.all()
        assert card_inner in deck_warrior.cards.all()