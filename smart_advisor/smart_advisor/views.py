from django.http import HttpResponse 

def success(request):
    return HttpResponse("Successful login.")
