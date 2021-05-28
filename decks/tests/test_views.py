import pytest
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate

from cards.tests.factories import UserFactory, CardFactory
from decks.tests.factories import DeckFactory
from decks.views import DeckViewSet

pytestmark = pytest.mark.django_db


class TestDeckViewSet:
    def test_deck_list(self, APIrequest):
        reverse_url = reverse("decks:decks-list")
        request = APIrequest.get(reverse_url)
        user = UserFactory()
        force_authenticate(request, user=user)
        response = DeckViewSet.as_view({"get": "list"})(request)

        assert response.status_code == 200
        assert "complete" not in response.data

    def test_decks_retrieve(self, APIrequest):
        deck = DeckFactory()
        reverse_url = reverse("decks:decks-detail", kwargs={"pk": deck.id})
        request = APIrequest.get(reverse_url)
        user = UserFactory()
        force_authenticate(request, user=user)
        response = DeckViewSet.as_view({"get": "retrieve"})(request, pk=deck.id)

        assert response.status_code == 200
        assert response.data["id"] == deck.id
        assert response.data["name"] == deck.name
        assert response.data["complete"] == deck.complete()

    def test_create_deck(self, APIrequest):
        card = CardFactory()
        card2 = CardFactory()
        user = UserFactory()
        values = {
            "name": "yisus",
            "size": 30,
            "hero_class_id": 9,
            "standard": True,
            "cards": [
                {"golden": True, "quantity": 1, "card": {"id": card.id}},
                {"golden": False, "quantity": 1, "card": {"id": card2.id}},
            ],
        }

        reverse_url = reverse("decks:decks-list")  # "http://localhost:8000/cards/cards"
        request = APIrequest.post(reverse_url, data=values, format="json")
        force_authenticate(request, user=user)
        response = DeckViewSet.as_view({"post": "create"})(request)

        assert response.status_code == 201
        # assert Deck.objects.filter(id=) == 1