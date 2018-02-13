from django.db import models

# Create your models here. --THIS is cust_data.models


class Address(models.Model):
    houseNum = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postCode = models.CharField(max_length=4)
    country = models.CharField(max_length=100)

    def __str__(self):
        return (self.houseNum + " " + self.street + " " + self.city + " " +
               self.state  + " " + self.postCode + " " + self.country)
 
class Person(models.Model):
    firstName = models.CharField(max_length=100)
    surName = models.CharField(max_length=100)
    DOB = models.DateField()
    residential = models.ForeignKey(Address, null=True, 
    on_delete=models.SET_NULL, related_name='res_addr')
    postal = models.ForeignKey(Address, null=True, 
    on_delete=models.SET_NULL, related_name='postal_addr')
