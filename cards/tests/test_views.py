import pytest
from rest_framework.test import APIRequestFactory
from cards.tests.factories import CardFactory, CollectionFactory, ExpansionFactory
from rest_framework.reverse import reverse
from cards.views import CardViewSet

pytestmark = pytest.mark.django_db


class TestCardViewSet:
    def test_cards_list(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(30, expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse("cards:cards-list")  # "http://localhost:8000/cards/cards"
        request = request_factory.get(reverse_url)
        response = CardViewSet.as_view({"get": "list"})(request)

        assert response.status_code == 200
        assert len(response.data) == 30
        assert "usage" not in response.data

    def test_cards_retrieve(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        cards = CardFactory.create_batch(30, expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-detail", kwargs={"pk": cards[0].id}
        )  # "http://localhost:8000/cards/cards/X"
        request = request_factory.get(reverse_url)
        response = CardViewSet.as_view({"get": "retrieve"})(request, pk=cards[0].id)

        assert response.status_code == 200
        assert response.data["id"] == cards[0].id
        assert response.data["name"] == cards[0].name
        assert response.data["usage"] == cards[0].usage()

    def test_cards_filter(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(100)
        card = CardFactory(expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"search": card.name})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["name"] == card.name
