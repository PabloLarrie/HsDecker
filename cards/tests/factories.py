from factory.django import DjangoModelFactory
from cards.models import Card, Collection, Expansion, HeroClass
from factory import Faker, SubFactory


class CollectionFactory(DjangoModelFactory):
    name = Faker("first_name")
    year = Faker("year")
    class Meta:
        model = Collection


class ExpansionFactory(DjangoModelFactory):
    name = Faker("first_name")
    collection = SubFactory(CollectionFactory)
    class Meta:
        model = Expansion


class CardFactory(DjangoModelFactory):
    expansion = SubFactory(ExpansionFactory)
    class Meta:
        model = Card


class HeroClassFactory(DjangoModelFactory):
    class Meta:
        model = HeroClass
