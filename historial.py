>>> from decks.serializers import DeckSerializer
>>> card1 = Card(name="vellen", cost=2)
>>> serializer = DeckSerializer(data={"name": "deck2", "cards":card1, "hero_class":10 })
>>> serializer.is_valid()
>>> serializer.save()
>>> car31 = DeckCard(deck_id=7, card_id=34, quantity=1, golden=False)
>>> car31.save()