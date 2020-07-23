import datetime
import factory
import random

from examples.models import *

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserOne

    name = "John Doe"

class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupOne

    name = "Admins"

class GroupLevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupLevel

    user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(GroupFactory)
    rank = 1

class UserWithGroupFactory(UserFactory):
    membership = factory.RelatedFactory(GroupLevelFactory, 'user')

class UserWith2GroupsFactory(UserFactory):
    membership1 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group1')
    membership2 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group2')