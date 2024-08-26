from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.init, name='init'),
    path('interesados', views.interested, name='interested'),
    path('welcome', views.welcome, name='welcome_procedures'),
]
