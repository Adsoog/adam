from django.urls import path
from .views import HomeCC

urlpatterns = [
     path('', HomeCC, name='home_cc'),
]
