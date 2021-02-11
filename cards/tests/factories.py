from factory.django import DjangoModelFactory
from cards.models import Card, Collection, Expansion, HeroClass
from factory import Faker, SubFactory


class CollectionFactory(DjangoModelFactory):
    name = Faker("name")
    year = Faker("year")
    class Meta:
        model = Collection


class ExpansionFactory(DjangoModelFactory):
    name = Faker("name")
    collection = SubFactory(CollectionFactory)
    class Meta:
        model = Expansion


class CardFactory(DjangoModelFactory):
    name = Faker("name")
    expansion = SubFactory(ExpansionFactory)
    cost = Faker("random_int", min=0, max=15)
    standard = True
    class Meta:
        model = Card


class HeroClassFactory(DjangoModelFactory):
    class Meta:
        model = HeroClass
