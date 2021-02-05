import pytest
from cards.models import Card, HeroClass 
from decks.models import Deck 
from cards.constants import QualityCard
from decks.tests.factories import CollectionFactory, ExpansionFactory


#Environments
@pytest.fixture
def env_coll():  
    return CollectionFactory()

@pytest.fixture
def env_exp(env_coll):  
    return ExtensionFactory(collection=env_coll)


#Classes
@pytest.fixture
def class_warrior(): 
    return HeroClass.objects.create(name="Warrior")

@pytest.fixture
def class_priest(): 
    return HeroClass.objects.create(name="Priest")


#Cards
@pytest.fixture
def card_vellen(env_exp): 
    # coll = CollectionFactory()
    # exp = ExpansionFactory(collection = coll) 
    return Card.objects.create(name="Prophet Vellen", quality=QualityCard.LEGENDARY, expansion=env_exp, cost=2)

@pytest.fixture
def card_control(class_priest, env_exp):
    # coll = CollectionFactory()
    # exp = ExpansionFactory(collection = coll) 
    cont = Card.objects.create(name="Mind Control", expansion=env_exp, cost=10)
    cont.heroes.set([class_priest])
    return cont

@pytest.fixture
def card_inner(class_warrior):
    coll = CollectionFactory()
    exp = ExpansionFactory(collection = coll) 
    inn = Card.objects.create(name="Inner Rage", expansion=exp, cost=0)
    inn.heroes.set([class_warrior])
    return inn

@pytest.fixture
def card_addict():
    coll = CollectionFactory()
    exp = ExpansionFactory(collection = coll) 
    return Card.objects.create(name="Mana Addict", expansion=exp, cost=1)


#Decks
@pytest.fixture
def deck_warrior(class_warrior): 
    return Deck.objects.create(name="deck", hero_class=class_warrior, size=30)

