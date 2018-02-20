from django.urls import path, include 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', views.not_yet, name='tbd'),
]
