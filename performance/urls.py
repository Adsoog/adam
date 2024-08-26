from django.urls import path
from .views import PerformanceView

urlpatterns = [
    path('performance/', PerformanceView.as_view(), name='performance'),
]
    