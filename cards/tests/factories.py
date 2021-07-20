from factory.django import DjangoModelFactory
from cards.models import Card, Collection, Expansion, HeroClass
from factory import Faker, SubFactory, Iterator
from cards.constants import TypeCard
from django.contrib.auth.models import User

# from django.contrib.auth import password_validation


class UserFactory(DjangoModelFactory):
    username = "user01"
    email = "user01@example.com"
    password = "user01P4ssw0rD"

    class Meta:
        model = User


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
    card_type = Iterator((c[0] for c in TypeCard.choices))

    class Meta:
        model = Card


class HeroClassFactory(DjangoModelFactory):
    name = Faker("pystr", max_chars=15)

    class Meta:
        model = HeroClass
