import factory
import datetime
from base import User, Log, GroupsUser, AdminUser, MyClass

# class UserFactory(factory.Factory):
#     class Meta:
#         model = User

#     first_name = "John"
#     last_name = "Doe"

class LogFactory(factory.Factory):
    class Meta:
        model = Log

    time_stamp = factory.LazyFunction(datetime.datetime.now)


class EnglishUserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = "John"
    last_name = "Doe"
    lang = 'en'

    first_name = factory.Sequence(lambda n: 'user%d' % n)
    lang = factory.Sequence(lambda n: 'lang%d' % n)
    last_name = factory.LazyAttribute(lambda obj: '%s@%s' %(obj.first_name, obj.lang))


class FrenchUserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = "Jean"
    last_name = "Dupont"
    lang = 'fr'


class UserFactory(factory.Factory):
    class Meta:
        model = GroupsUser

    firstname = "John"
    lastname = "Doe"
    group = 'users'

class AdminFactory(UserFactory):
    class Meta:
        model = AdminUser
    admin = True
    group = 'admins'

class MyFactory(factory.Factory):
    class Meta:
        model = MyClass
    obj_number = factory.Sequence(lambda n: 'user%d' % n)