import pytest

from decks.tests.factories import DeckFactory, DeckCardFactory
from cards.tests.factories import CardFactory, HeroClassFactory, ExpansionFactory
from cards.constants import QualityCard

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.test import APIRequestFactory


@pytest.fixture
def APIrequest():
    return APIRequestFactory()


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
    return CardFactory(quality=QualityCard.LEGENDARY)


@pytest.fixture
def card_priest(class_priest):
    pri = CardFactory()
    pri.heroes.set([class_priest])
    return pri


@pytest.fixture
def card_priest_savage(class_priest):
    pri = CardFactory(standard=False)
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
def deck_priest_savage(class_priest):
    return DeckFactory(hero_class=class_priest, standard=False)


@pytest.fixture(autouse=True)
def disable_authentication(monkeypatch, request):
    """
    Use `use_auth` marker to enable authentication for the test.
    See https://pytest.readthedocs.io/en/latest/example/markers.html
    """
    if "use_auth" not in request.keywords:
        monkeypatch.setattr(APIView, "permission_classes", (AllowAny,))