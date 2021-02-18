>>> from decks.serializers import DeckSerializer
>>> card1 = Card(name="vellen", cost=2)
>>> serializer = DeckSerializer(data={"name": "deck2", "cards":card1, "hero_class":10 })
>>> serializer.is_valid()
>>> serializer.save()
>>> car31 = DeckCard(deck_id=7, card_id=34, quantity=1, golden=False)
>>> car31.save()

Aitor Bouzas Naveira
16:43
{
  "name": "Mi mazo",
  "size": 30,
  "hero_class": "Warrior",
  "cards": [
    {
      "quantity": 1,
      "golden": true,
      "card": {
        "name": "Prophet of Vellen",
        "cost": 7,
        "attack": 6
      }
    }
  ]
}