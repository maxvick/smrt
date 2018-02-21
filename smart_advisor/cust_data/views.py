from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.views.generic.edit import UpdateView
from .models import Person

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def not_yet(request):
    return HttpResponse("nothing defd yet")

class PersonUpdate(UpdateView):
    model = Person
    fields = [
             'firstName',
             ]
    template_name_suffix = '_update_form'
