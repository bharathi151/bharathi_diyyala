from django.db import models

# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    brand_score=models.IntegerField()
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=150)
    average_rating=models.IntegerField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    
class Pan_Details(models.Model):
    number=models.IntegerField()
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    verifiedcd=models.BooleanField()
    

class Customer(models.Model):
    name=models.CharField(max_length=50)
    mobile_number=models.IntegerField()
    email_address=models.CharField(max_length=100)
    pan_card=models.OneToOneField(Pan_Details,on_delete=models.CASCADE)
    
    
class Order(models.Model):
    products=models.ManyToManyField(Product)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_value=models.IntegerField()
    delivery_date=models.DateField()
    purchase_date=models.DateField()
    