import pytest
from decks.models import Deck, DeckCard
from cards.models import Card, HeroClass, Collection, Expansion


pytestmark = pytest.mark.django_db
class TestCards:

    def test_usage(self):
        wa = HeroClass(name="Warrior")
        wa.save()
        coll1 = Collection(name="Main Collection", year=2014)
        coll1.save()
        exp1 = Expansion(name="Basic", collection=coll1)
        exp1.save()
        vellen = Card(name="Prophet Vellen", expansion=exp1, cost=2)
        vellen.save()
        croko = Card(name="Crokolisk", expansion=exp1, cost=2)
        croko.save()
        deck1 = Deck(name="deck1", hero_class=wa, size=30)
        deck1.save()
        deck2 = Deck(name="deck2", hero_class=wa, size=30)
        deck2.save()
        DeckCard(deck=deck2, card=vellen, quantity=2, golden=False).save()
        DeckCard(deck=deck2, card=croko, quantity=1, golden=True).save()        
        DeckCard(deck=deck1, card=croko, quantity=1, golden=False).save()
        DeckCard(deck=deck1, card=croko, quantity=1, golden=True).save()
        assert vellen.usage() == 50
        assert croko.usage() == 100