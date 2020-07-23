import datetime
import factory
import random

from examples.models import *

class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Iterator(["France", "Italy", "Spain"])
    lang = factory.Iterator(['fr', 'it', 'es'])

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    name = "John"
    lang = factory.SelfAttribute('country.lang')
    country = factory.SubFactory(CountryFactory)

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = "ACME, Inc."
    country = factory.SubFactory(CountryFactory)
    owner = factory.SubFactory(UserFactory, country=factory.SelfAttribute('..country'))

class CompanyOwnerWithFactoryName(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = "ACME, Inc."
    country = factory.SubFactory(CountryFactory)
    owner = factory.SubFactory(UserFactory,
        name=factory.LazyAttribute(lambda obj:"OwnerOf %s" %obj.factory_parent.name))

