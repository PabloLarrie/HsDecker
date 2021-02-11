import pytest
from decks.models import DeckCard
from decks.tests import factories


pytestmark = pytest.mark.django_db
class TestDecks:
    
    def test_legendary_uniqueness(self, card_legendary, deck_warrior):
        with pytest.raises(ValueError):
            DeckCard(deck=deck_warrior, card=card_legendary, quantity=2, golden=False).save()
        DeckCard(deck=deck_warrior, card=card_legendary, quantity=1, golden=False).save()
        with pytest.raises(ValueError):
            DeckCard(deck=deck_warrior, card=card_legendary, quantity=1, golden=False).save()
        

    def test_same_class(self, card_priest, card_warrior, card_neutral, deck_warrior):
        DeckCard(deck=deck_warrior, card=card_warrior, quantity=2, golden=False).save()
        with pytest.raises(ValueError):
            DeckCard(deck=deck_warrior, card=card_priest, quantity=2, golden=False).save()

        DeckCard(deck=deck_warrior, card=card_neutral, quantity=2, golden=False).save()

        assert card_neutral in deck_warrior.cards.all()
        assert card_warrior in deck_warrior.cards.all()


    def test_complete(self, deck_priest, card_priest):
        factories.DeckCardFactory.create_batch(14, deck=deck_priest, quantity=2)
        DeckCard(deck=deck_priest, card=card_priest, quantity=1, golden=True).save()
        DeckCard(deck=deck_priest, card=card_priest, quantity=1, golden=False).save()

        deck_priest.size = 30
        assert deck_priest.complete() 
        deck_priest.size = 28
        assert not deck_priest.complete() 