from django.urls import path
from .views import CombinedFormView, assign_resource

urlpatterns = [
    path('create/', CombinedFormView.as_view(), name='create-resource-hazard'),
]
