from django.db import models

# Create your models here.

class Customers(models.Model):
    cust_name=models.CharField(max_length=50)
    cust_email=models.EmailField()
    cust_contact=models.IntegerField()
    cust_password=models.CharField(max_length=50)
