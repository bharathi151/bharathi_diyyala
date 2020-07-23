from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=100)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class UserOne(models.Model):
    name = models.CharField(max_length=100)

class GroupOne(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(UserOne, through='GroupLevel')

class GroupLevel(models.Model):
    user = models.ForeignKey(UserOne, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupOne, on_delete=models.CASCADE)
    rank = models.IntegerField()

class Country(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)

class Person(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

# from datetime import date
# class Account(models.Model):
#     username = models.CharField(max_length=100,primary_key=True)
#     email = models.CharField(max_length=100, unique=True)
#     date_joined = models.DateField()

# class Profile(models.Model):
#     gender_choices=(('FEMALE','f'),
#     ('MALE','m'),
#     ('NOT-INTRESTED-TO-SAY','u'))
#     gender = models.CharField(max_length=100,choices=gender_choices)
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     planet = models.CharField(max_length=100)
#     account = models.OneToOneField(Account,on_delete=models.CASCADE)
