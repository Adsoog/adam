from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import EPPS

class EPPSListView(ListView):
    model = EPPS
    template_name = 'epps/epps_list.html' 
    context_object_name = 'epps'

class EPPSDetailView(DetailView):
    model = EPPS
    template_name = 'epps/epps_detail.html' 

class EPPSCreateView(CreateView):
    model = EPPS
    template_name = 'epps/epps_form.html' 
    fields = '__all__'
    success_url = reverse_lazy('epps-list')

class EPPSUpdateView(UpdateView):
    model = EPPS
    template_name = 'epps/epps_form.html' 
    fields = '__all__'
    success_url = reverse_lazy('epps-list')

class EPPSDeleteView(DeleteView):
    model = EPPS
    template_name = 'epps/epps_confirm_delete.html' 
    success_url = reverse_lazy('epps-list')
