from django.db import models
from cust_data.models import Person
from django.db.models import Sum

# Create your models here. --THIS is finance.models
#class Account(models.Model):
#    name = models.CharField(max_length=100)
#    parent = models.IntegerField(null=True)
#    owner = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)

#    def getBalance(self, start=None, end=None):
        #get all of the transactions belonging to this account
#        linkedTrans = Transaction.objects.get(account__exact=self)
        
        #end of getBalance
#        return linkedTrans.aggregate(Sum('value'))

#class Transaction(models.Model):
#    account = models.ForeignKey(Account, on_delete=models.CASCADE)
#    value = models.DecimalField(max_digits=25, decimal_places=2)
#    t_date = models.DateField()
