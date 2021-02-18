import pytest
from cards.constants import QualityCard
from decks.tests.factories import DeckFactory, DeckCardFactory
from cards.tests.factories import CardFactory, HeroClassFactory, ExpansionFactory


@pytest.fixture
def expansion_1(): 
    return ExpansionFactory()


@pytest.fixture
def class_warrior(): 
    return HeroClassFactory(name="Warrior")

@pytest.fixture
def class_priest(): 
    return HeroClassFactory(name="Priest")



@pytest.fixture
def card_legendary(): 
    return CardFactory (quality=QualityCard.LEGENDARY)

@pytest.fixture
def card_priest(class_priest):
    pri = CardFactory()
    pri.heroes.set([class_priest])
    return pri

@pytest.fixture
def card_priest_savage (class_priest): 
    pri = CardFactory(standard = False)
    pri.heroes.set([class_priest])
    return pri

@pytest.fixture
def card_warrior(class_warrior): 
    warr = CardFactory()
    warr.heroes.set([class_warrior])
    return warr

@pytest.fixture
def card_neutral():
    return CardFactory()



@pytest.fixture
def deck_warrior(class_warrior): 
    return DeckFactory(hero_class=class_warrior)

@pytest.fixture
def deck_priest(class_priest): 
    return DeckFactory(hero_class=class_priest)

@pytest.fixture
def deck_priest_savage (class_priest): 
    return DeckFactory(hero_class=class_priest, standard=False)

