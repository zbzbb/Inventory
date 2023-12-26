from django.db import models
class Category (models.Model):
    code = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
class Product (models.Model):
    code = models.CharField(max_length=255, null=True)
    desc = models.CharField(max_length=255, null=True)
    count = models.IntegerField(null=True)
class Supplier (models.Model):
    idettity = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
class invention (models.Model):
    product_code = models.CharField(max_length=255, null=True)
    supplier_code = models.CharField(max_length=255, null=True)
    count = models.IntegerField()
    date = models.DateField()
