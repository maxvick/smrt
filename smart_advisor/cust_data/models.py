from django.db import models
from django.urls import reverse
from django.db.models import Sum, Q

# Create your models here. --THIS is cust_data.models


class Address(models.Model):
    house_number = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postCode = models.CharField(max_length=4)
    country = models.CharField(max_length=100)

    def __str__(self):
        return (self.house_number + " " + self.street + " " + self.city + " " +
               self.state  + " " + self.postCode + " " + self.country)
 
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    residential_address = models.ForeignKey(Address, null=True, 
    on_delete=models.SET_NULL, related_name='res_addr')
    postal_address = models.ForeignKey(Address, null=True, 
    on_delete=models.SET_NULL, related_name='postal_addr')

    def listAccounts(self):
        retVal = [] #placeholder for list of tuples acc + balance

        #get a queryset of all of person's accounts
        myAcc = Account.objects.filter(owner==self.id)
        
        myAcc = myAcc.annotate(balance=Sum('transaction__value'))
        
        #end of listAccounts
        return myAcc

    def get_absolute_url(self):
        #end of gau
        return reverse('person-detail', kwargs={'pk': self.pk})

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

