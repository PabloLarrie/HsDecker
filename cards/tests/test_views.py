import pytest

from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.reverse import reverse

from cards.tests.factories import (
    CardFactory,
    CollectionFactory,
    ExpansionFactory,
    UserFactory,
)
from cards.views import CardViewSet
from cards.serializers import CardSerializer
from cards.models import Card

from django.contrib.auth.models import User


pytestmark = pytest.mark.django_db


class TestCardViewSet:
    def test_cards_list(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        request_factory = APIRequestFactory()
        reverse_url = reverse("cards:cards-list")  # "http://localhost:8000/cards/cards"
        cards = CardFactory.create_batch(10, expansion=expansion)
        request = request_factory.get(reverse_url)
        user = UserFactory()
        force_authenticate(request, user=user)
        response = CardViewSet.as_view({"get": "list"})(request)

        assert response.status_code == 200
        assert len(response.data["results"]) == 10
        assert "usage" not in response.data

        reverse_url = reverse("cards:cards-detail", kwargs={"pk": cards[0].id})
        request = request_factory.get(reverse_url)
        force_authenticate(request, user=user)
        response = CardViewSet.as_view({"get": "retrieve"})(request, pk=cards[0].id)
        assert response.status_code == 200
        assert response.data["id"] == cards[0].id
        assert response.data["name"] == cards[0].name
        assert response.data["usage"] == cards[0].usage()

    def test_cards_filters(self, class_priest, card_legendary):
        user = UserFactory()

        def assert_filter(request, filters):
            force_authenticate(request, user=user)
            response = CardViewSet.as_view({"get": "list"})(request)
            assert response.status_code == 200
            result_cards_ids = list(
                Card.objects.filter(**filters).values_list("id", flat=True)
            )
            assert all(
                [
                    result["id"] in result_cards_ids
                    for result in response.data["results"]
                ]
            )

        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10, standard=False, cost=2)
        card = CardFactory(
            expansion=expansion, race="beast", cost=1, card_type="minion"
        )
        card.heroes.set([class_priest])
        card_legendary.cost = 3
        card_legendary.standard = False
        card_legendary.save()

        request_factory = APIRequestFactory()
        reverse_url = reverse("cards:cards-list")

        request = request_factory.get(reverse_url, {"search": card.name})
        force_authenticate(request, user=user)
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["name"] == card.name

        request = request_factory.get(reverse_url, {"search": card.card_type})
        force_authenticate(request, user=user)
        response = CardViewSet.as_view({"get": "list"})(request)
        assert response.status_code == 200
        assert all(
            [
                result["card_type"] == card.card_type
                for result in response.data["results"]
            ]
        )

        request = request_factory.get(reverse_url, {"search": card_legendary.quality})
        assert_filter(request, {"quality": card_legendary.quality})

        request = request_factory.get(reverse_url, {"hero": class_priest.id})
        assert_filter(request, {"heroes": class_priest})

        request = request_factory.get(reverse_url, {"race": card.race})
        assert_filter(request, {"race": card.race})

        request = request_factory.get(reverse_url, {"expansion": expansion.id})
        assert_filter(request, {"expansion": card.expansion})

        request = request_factory.get(reverse_url, {"cost": card.cost})
        assert_filter(request, {"cost": card.cost})

        request = request_factory.get(reverse_url, {"standard": card.standard})
        assert_filter(request, {"standard": card.standard})

    def test_create_card(self, expansion_1):
        user = UserFactory()

        values = {
            "expansion": {"id": expansion_1.id},
            "description": "yisus",
            "race": "beast",
            "name": "Vellen",
            "cost": 2,
        }

        request_factory = APIRequestFactory()
        reverse_url = reverse("cards:cards-list")  # "http://localhost:8000/cards/cards"
        request = request_factory.get(reverse_url)
        force_authenticate(request, user=user)
        response = CardViewSet.as_view({"get": "list"})(request)
        create = response({"post": "create"})(values)

        assert create.status_code == 200
