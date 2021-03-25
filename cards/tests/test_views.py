import pytest
from rest_framework.test import APIRequestFactory
from cards.tests.factories import CardFactory, CollectionFactory, ExpansionFactory
from rest_framework.reverse import reverse
from cards.views import CardViewSet
from cards.serializers import CardSerializer
from cards.models import Card


pytestmark = pytest.mark.django_db


class TestCardViewSet:
    def test_cards_list(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        request_factory = APIRequestFactory()
        reverse_url = reverse("cards:cards-list")  # "http://localhost:8000/cards/cards"
        cards = CardFactory.create_batch(10, expansion=expansion)
        request = request_factory.get(reverse_url)

        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data["results"]) == 10
        assert "usage" not in response.data

        reverse_url = reverse("cards:cards-detail", kwargs={"pk": cards[0].id})
        response = CardViewSet.as_view({"get": "retrieve"})(request, pk=cards[0].id)
        assert response.status_code == 200
        assert response.data["id"] == cards[0].id
        assert response.data["name"] == cards[0].name
        assert response.data["usage"] == cards[0].usage()

    def test_cards_filters(self, class_priest, card_legendary):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10, standard=False, cost=2)
        card = CardFactory(expansion=expansion, race="beast", cost=1)
        card.heroes.set([class_priest])
        card_legendary.cost = 3
        # card_legendary.standard = False

        request_factory = APIRequestFactory()
        reverse_url = reverse("cards:cards-list")
        request = request_factory.get(reverse_url, {"search": card.name})
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["name"] == card.name

        request = request_factory.get(reverse_url, {"search": card.card_type})
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert response.data["results"][0]["card_type"] == card.card_type

        request = request_factory.get(reverse_url, {"hero": class_priest.id})
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id

        request = request_factory.get(reverse_url, {"race": card.race})
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id

        request = request_factory.get(reverse_url, {"expansion": expansion.id})
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id

        request = request_factory.get(reverse_url, {"cost": card.cost})
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id

        request = request_factory.get(reverse_url, {"standard": card.standard})
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data["results"]) == 2
        assert response.data["results"][1]["id"] == card.id
        # Malamente arreglado

        request = request_factory.get(reverse_url, {"search": card_legendary.quality})
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert response.data["results"][0]["quality"] == card_legendary.quality

    def test_create_card(self, expansion_1):
        values = {
            "expansion": {"id": expansion_1.id},
            "description": "yisus",
            "race": "beast",
            "name": "Vellen",
            "cost": 2,
        }
        serializer = CardSerializer(data=values)
        assert serializer.is_valid()
        serializer.save()
        assert Card.objects.filter(name=values["name"])
