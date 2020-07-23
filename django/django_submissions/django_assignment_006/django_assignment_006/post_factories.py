import datetime
import factory
import random


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = "John"
    profile_pic = "profile_pic"