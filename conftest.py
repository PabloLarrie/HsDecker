import pytest
from cards.models import Card, HeroClass 
from decks.models import Deck 
from cards.constants import QualityCard
from decks.tests.factories import CollectionFactory, ExpansionFactory



# @pytest.fixture
# def default_collection():  
#     return CollectionFactory()

@pytest.fixture
def default_expansion():  
    return ExpansionFactory()



@pytest.fixture
def class_warrior(): 
    return HeroClass.objects.create(name="Warrior")

@pytest.fixture
def class_priest(): 
    return HeroClass.objects.create(name="Priest")



@pytest.fixture
def card_legendary(default_expansion): 
    return Card.objects.create(name="Prophet Vellen", quality=QualityCard.LEGENDARY, expansion=default_expansion, cost=2)

@pytest.fixture
def card_priest(class_priest, default_expansion):
    cont = Card.objects.create(name="Mind Control", expansion=default_expansion, cost=10)
    cont.heroes.set([class_priest])
    return cont

@pytest.fixture
def card_warrior(class_warrior, default_expansion): 
    inn = Card.objects.create(name="Inner Rage", expansion=default_expansion, cost=0)
    inn.heroes.set([class_warrior])
    return inn

@pytest.fixture
def card_neutral(default_expansion):
    return Card.objects.create(name="Mana Addict", expansion=default_expansion, cost=1)



@pytest.fixture
def deck_warrior(class_warrior): 
    return Deck.objects.create(name="deck", hero_class=class_warrior, size=30)

@pytest.fixture
def deck_priest(class_priest): 
    return Deck.objects.create(name="deck2", hero_class=class_priest, size=30)

