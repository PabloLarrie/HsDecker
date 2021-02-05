from factory.django import DjangoModelFactory
from cards.models import Collection, Expansion
from factory import Faker

class CollectionFactory(DjangoModelFactory):
    name = Faker("first_name")
    year = Faker("year")
    
    
    class Meta:
        model = Collection

class ExpansionFactory(DjangoModelFactory):
    name = Faker("first_name")
    #collection = CollectionFactory

    class Meta:
        model = Expansion
