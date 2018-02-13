from django.contrib import admin

# Register your models here.
from .models import Address
from .models import Person
from .models import Account
from .models import Transaction

admin.site.register(Address)
admin.site.register(Person)
admin.site.register(Account)
admin.site.register(Transaction)
