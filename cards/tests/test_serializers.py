import pytest
from cards.serializers import CardSerializer
from cards.models import Card, Expansion


pytestmark = pytest.mark.django_db
class TestCardsSerializers: 

    def test_create_card(self, expansion_1):
        values_error = {"expansion": {"id": 9}, "name": "Vellen", "cost": 2}
        serializer = CardSerializer(data=values_error)
        serializer.is_valid()
        with pytest.raises(Expansion.DoesNotExist):
            serializer.save()

        values = {"expansion": {"id": expansion_1.id}, "name": "Vellen", "cost": 2}
        serializer = CardSerializer(data=values)
        
        assert serializer.is_valid() 
        serializer.save()
        assert Card.objects.filter(name=values["name"])
