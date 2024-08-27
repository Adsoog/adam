# projects/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from .views import (
    ContractorListView, ContractorDetailView, ContractorCreateView, ContractorUpdateView, ContractorDeleteView,
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)


urlpatterns = [
    path('contractors/', ContractorListView.as_view(), name='contractor_list'),
    path('contractors/<int:pk>/', ContractorDetailView.as_view(), name='contractor_detail'),
    path('contractors/add/', ContractorCreateView.as_view(), name='contractor_add'),
    path('contractors/<int:pk>/edit/', ContractorUpdateView.as_view(), name='contractor_edit'),
    path('contractors/<int:pk>/delete/', ContractorDeleteView.as_view(), name='contractor_delete'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/add/', ClientCreateView.as_view(), name='client_add'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_add'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    
    #API REST
    path('api', include(router.urls)),
    

]
