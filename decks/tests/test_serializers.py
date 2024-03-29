import pytest
from decks.serializers import DeckSerializer, DeckSimpleSerializer
from decks.models import Deck, DeckCard
from decks.tests import factories


pytestmark = pytest.mark.django_db

# TODO: create correct serializer tests

# class TestDecksSerializers:
#     def test_create_deck(self):
#         serializer = DeckSimpleSerializer(data={"name": "mideck"})
#         assert serializer.is_valid()
#         assert serializer.save()
#
#     def test_deck_cards(self, card_neutral):
#         serializer = DeckSerializer(data={"name": "mideck"})
#         assert serializer.is_valid()
#         deck = serializer.save()
#         DeckCard(deck_id=deck.id, card=card_neutral, quantity=2, golden=False).save()
