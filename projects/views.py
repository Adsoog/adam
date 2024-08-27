# projects/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contractor, Client, Project
from .forms import ContractorForm, ClientForm, ProjectForm

class ContractorListView(ListView):
    model = Contractor
    template_name = 'contractor/contractor_list.html'

class ContractorDetailView(DetailView):
    model = Contractor
    template_name = 'contractor/contractor_detail.html'

class ContractorCreateView(CreateView):
    model = Contractor
    form_class = ContractorForm
    template_name = 'contractor/contractor_form.html'
    success_url = reverse_lazy('contractor_list')

class ContractorUpdateView(UpdateView):
    model = Contractor
    form_class = ContractorForm
    template_name = 'contractor/contractor_form.html'
    success_url = reverse_lazy('contractor_list')

class ContractorDeleteView(DeleteView):
    model = Contractor
    template_name = 'contractor/contractor_confirm_delete.html'
    success_url = reverse_lazy('contractor_list')

# CLIENT 
class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

# PROJECT
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

# API REST
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer