from email.quoprimime import body_check
from turtle import heading
from django.db import models

# Create your models here.

class People(models.Model):
    people_title = models.CharField(max_length=100)
    people_name= models.CharField(max_length= 100)
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.people_title


class Address(models.Model):
    home_address = models.CharField(max_length= 100)
    postcode = models.CharField(max_length = 20)
    address_owner = models.ForeignKey(People, on_delete= models.CASCADE)

    def __str__(self):
            return self.postcode

class Doctor(models.Model):
    doctor_name= models.CharField(max_length = 20)
    patients = models.ForeignKey(People, on_delete= models.CASCADE)

    def __str__(self):
            return self.doctor_name

class Product(models.Model):
    product_name = models.CharField(max_length = 20)
    product_category = models.CharField(max_length= 20)
    product_price = models.CharField(max_length = 10)

    def __str__(self):
            return self.product_name

class Bio(models.Model):
    gender= models.CharField(max_length = 10)
    email = models.EmailField(default= "ofoh@gmail.com")
    age= models.CharField(max_length= 3)
    friends= models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
            return self.gender



