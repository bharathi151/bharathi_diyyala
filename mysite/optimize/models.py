from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
class Author(models.Model):
    name = models.CharField(max_length=200, default='')

class Book(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='books',
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    title = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')

    def get_page_count(self):
        return self.pages.count()

class Page(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='pages',
    )
    text = models.TextField(null=True, blank=True)
    page_number = models.IntegerField()

#select_related in querying
#prefetch_related

from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

   
class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by', on_delete=models.CASCADE)