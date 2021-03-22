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
        CardFactory.create_batch(10, expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse("cards:cards-list")  # "http://localhost:8000/cards/cards"
        request = request_factory.get(reverse_url)
        response = CardViewSet.as_view({"get": "list"})(request)

        result = [y for v in response.data.values() if type(v) == list for y in v]

        assert response.status_code == 200
        assert len(result) == 10
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
        CardFactory.create_batch(10)
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

    def test_cards_typefilter(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10)
        card = CardFactory(expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"search": card.card_type})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        # assert len(response.data) == 1
        assert response.data[0]["card_type"] == card.card_type

    def test_cards_standardfilter(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10, standard=False)
        card = CardFactory(expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"standard": card.standard})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["id"] == card.id

    def test_cards_herofilter(self, class_priest):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10)
        card = CardFactory(expansion=expansion)
        card.heroes.set([class_priest])

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"hero": class_priest.id})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        # assert len(response.data) == 1
        assert response.data[0]["id"] == card.id

    def test_cards_qualityfilter(self, card_legendary):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10)
        # card = CardFactory(expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"search": card_legendary.quality})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        # assert len(response.data) == 1
        assert response.data[0]["quality"] == card_legendary.quality

    def test_cards_racefilter(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10)
        card = CardFactory(expansion=expansion, race="")

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"search": card.race})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        # assert len(response.data) == 1
        assert response.data["race"] == card.race

    def test_cards_expansionfilter(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10)
        card = CardFactory(expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"search": card.expansion})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        # assert len(response.data) == 1
        assert response.data[0]["expansion"] == card.expansion

    def test_cards_costfilter(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10)
        card = CardFactory(expansion=expansion, cost=1)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"search": card.cost})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        # assert len(response.data) == 1
        assert response.data[0]["expansion"] == card.cost

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