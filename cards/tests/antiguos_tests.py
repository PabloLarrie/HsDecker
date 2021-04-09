
    def test_cards_list(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10, expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse("cards:cards-list")  # "http://localhost:8000/cards/cards"
        request = request_factory.get(reverse_url)
        response = CardViewSet.as_view({"get": "list"})(request)

        # result = [y for v in response.data.values() if type(v) == list for y in v]

        assert response.status_code == 200
        assert len(response.data["results"]) == 10
        assert "usage" not in response.data

    def test_cards_retrieve(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        cards = CardFactory.create_batch(10, expansion=expansion)

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


    
    def test_cards_filters(self):
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
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["name"] == card.name


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
        assert response.data["results"][0]["card_type"] == card.card_type

    
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
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id


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
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id

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
        # assert response.data["results"] == 1
        assert response.data["results"][0]["quality"] == card_legendary.quality

    def test_cards_racefilter(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10)
        card = CardFactory(expansion=expansion, race="beast")

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"race": card.race})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id


        def test_cards_expansionfilter(self):
            collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10)
        card = CardFactory(expansion=expansion)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"expansion": expansion.id})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id


    def test_cards_costfilter(self):
        collection = CollectionFactory()
        expansion = ExpansionFactory(collection=collection)
        CardFactory.create_batch(10, cost=5)
        card = CardFactory(expansion=expansion, cost=1)

        request_factory = APIRequestFactory()
        reverse_url = reverse(
            "cards:cards-list"
        )  # "http://localhost:8000/cards/cards/X" (URL correspondiente al listado de cartas)
        request = request_factory.get(reverse_url, {"cost": card.cost})
        response = CardViewSet.as_view({"get": "list"})(request)
        # devuelve el método que se encarga de devolver la lista de cartas if request

        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["id"] == card.id