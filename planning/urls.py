from django.urls import include, path
from .views import planning_homepage, create_station, station_detail


urlpatterns = [
    path('', planning_homepage, name='planning_homepage'),
    path('create-station/<int:project_id>/', create_station, name='create_station'),
    path('station/<int:station_id>/', station_detail, name='station_detail'),
]