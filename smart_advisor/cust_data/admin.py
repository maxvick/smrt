from django.contrib import admin

# Register your models here.
from .models import Address
from .models import Person

admin.site.register(Address)
admin.site.register(Person)
