from django.db import models

# Create your models here.


class Address(models.Model):
    houseNum = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postCode = models.CharField(max_length=4)
    country = models.CharField(max_length=100)
 
class Person(models.Model):
    firstName = models.CharField(max_length=100)
    surName = models.CharField(max_length=100)
    residential = models.ForeignKey(Address, null=True, 
    on_delete=models.SET_NULL, related_name='res_addr')
    postal = models.ForeignKey(Address, null=True, 
    on_delete=models.SET_NULL, related_name='postal_addr')
