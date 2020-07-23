import datetime
import factory
import random

from examples.models import *


# class AccountFactory(factory.Factory):
#     class Meta:
#         model = Account

#     username = factory.Sequence(lambda n: 'john%s' % n)
#     email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
#     date_joined = factory.LazyFunction(datetime.datetime.now)


# class ProfileFactory(factory.Factory):
#     class Meta:
#         model = Profile

#     account = factory.SubFactory(AccountFactory)
#     gender = factory.Iterator(["MALE", "FEMALE"])
#     firstname = u'John'
#     lastname = u'Doe'
class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group
    group_name = factory.Sequence(lambda n: "Group %d" %n)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    group = factory.SubFactory(GroupFactory)

