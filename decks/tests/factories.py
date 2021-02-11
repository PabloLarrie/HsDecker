from factory.django import DjangoModelFactory
from decks.models import Deck, DeckCard
from cards.tests.factories import HeroClassFactory, CardFactory
from factory import Faker, SubFactory


class DeckFactory(DjangoModelFactory):
    hero_class = SubFactory(HeroClassFactory)
    standard = False
    class Meta:
        model = Deck


class DeckCardFactory(DjangoModelFactory):
    deck = SubFactory(DeckFactory)
    card = SubFactory(CardFactory)
    quantity = Faker("random_int", min=1, max=2)
    golden = False
    class Meta:
        model = DeckCard 
