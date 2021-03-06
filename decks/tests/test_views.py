import pytest
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.reverse import reverse

from decks.tests.factories import DeckFactory
from cards.tests.factories import UserFactory
from decks.views import DeckViewSet

pytestmark = pytest.mark.django_db


class TestDeckViewSet:
    def test_deck_list(self):
        DeckFactory()
        request_factory = APIRequestFactory()
        reverse_url = reverse("decks:decks-list")
        request = request_factory.get(reverse_url)
        user = UserFactory()
        force_authenticate(request, user=user)
        response = DeckViewSet.as_view({"get": "list"})(request)

        assert response.status_code == 200
        assert "complete" not in response.data

    def test_decks_retrieve(self):
        deck = DeckFactory()
        request_factory = APIRequestFactory()
        reverse_url = reverse("decks:decks-detail", kwargs={"pk": deck.id})
        request = request_factory.get(reverse_url)
        user = UserFactory()
        force_authenticate(request, user=user)
        response = DeckViewSet.as_view({"get": "retrieve"})(request, pk=deck.id)

        assert response.status_code == 200
        assert response.data["id"] == deck.id
        assert response.data["name"] == deck.name
        assert response.data["complete"] == deck.complete()

    def test_create_deck(self, APIrequest):
        user = UserFactory()
        values = {
            "name": "yisus",
            "size": 30,
            "hero_class_id": 9,
            "standard": True,
        }

        reverse_url = reverse("decks:decks-list")  # "http://localhost:8000/cards/cards"
        request = APIrequest.post(reverse_url, data=values, format="json")
        force_authenticate(request, user=user)
        response = DeckViewSet.as_view({"post": "create"})(request)

        assert response.status_code == 201
        # assert Card.objects.all() == 1