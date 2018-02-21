from django.urls import path, include 
from . import views 
from .views import PersonUpdate

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', views.not_yet, name='tbd'),
    path('person/<int:pk>/', PersonUpdate.as_view(), name='person-update'),
]
