from django.db import models
from django.db.models import Sum
from django.db.models import Q

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

class Account(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def getBalance(self, start=None, end=None):
        retVal = 0

        #get all of the transactions belonging to this account
        linkedTrans = Transaction.objects.filter(account__exact=self)

        if (start is None and end is None):
            retVal = linkedTrans.aggregate(Sum('value'))

        elif (start is None):
            retVal = linkedTrans.filter(t_date__lte=end).aggregate(Sum('value'))

        elif (end is None):
            retVal = linkedTrans.filter(t_date__gte=start).aggregate(Sum('value'))

        else:
            retVal = linkedTrans.filter(Q(t_date__gte=start) &
            Q(t_date__lte=end)).aggregate(Sum('value'))

        if retVal['value__sum'] is None:
            retVal = 0

        else:
            retVal = retVal['value__sum']

        #end of getBalance
        return retVal

    def getTotalChildBalance(self, start=None, end=None):
        retVal = 0

        #get all of the child accounts
        childAccs = Account.objects.filter(parent=self.id)

        #loop and aggregate the values
        for acc in childAccs:
            retVal += acc.getBalance(start, end)

        #end of getChildBalance
        return retVal

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=25, decimal_places=2)
    t_date = models.DateField()
    description = models.CharField(max_length=100, blank=True, null=True)

