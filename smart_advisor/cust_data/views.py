from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from .models import Person

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def not_yet(request):
    return HttpResponse("nothing defd yet")

class PersonDetail(DetailView):
    model = Person

class PersonUpdate(UpdateView):
    model = Person
    fields = [
             'first_name',
             'last_name',
	     'date_of_birth',
             'postal_address',
             ]
    template_name_suffix = '_update_form'
