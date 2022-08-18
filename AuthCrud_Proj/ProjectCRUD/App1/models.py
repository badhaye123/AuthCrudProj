from django.db import models

# Create your models here.

s_c=(('Amazon','Amazon'),
     ('Flipkart','Flipkart'),
     ('Myntra','Myntra'),
     ('Ebay','Ebay'),
     ('Bigbasket','Bigbasket'))
p=(('Clothes','Clothes'),('Mobile','Mobile'),('Laptop','Laptop'),('Chair','Chair'),('Grocery','Grocery'))



class Orders(models.Model):
    seller=models.CharField(max_length=34,choices=s_c)
    product=models.CharField(max_length=34,choices=p)
    quantity=models.IntegerField()
    price=models.FloatField()
    is_paid=models.BooleanField()
