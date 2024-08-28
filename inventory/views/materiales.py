from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Materiales

class MaterialesListView(ListView):
    model = Materiales
    template_name = 'materiales/materiales_list.html' 
    context_object_name = 'materiales'

class MaterialesDetailView(DetailView):
    model = Materiales
    template_name = 'materiales/materiales_detail.html'  

class MaterialesCreateView(CreateView):
    model = Materiales
    template_name = 'materiales/materiales_form.html' 
    fields = '__all__'
    success_url = reverse_lazy('materiales-list')

class MaterialesUpdateView(UpdateView):
    model = Materiales
    template_name = 'materiales/materiales_form.html'  
    fields = '__all__'
    success_url = reverse_lazy('materiales-list')

class MaterialesDeleteView(DeleteView):
    model = Materiales
    template_name = 'materiales/materiales_confirm_delete.html'
    success_url = reverse_lazy('materiales-list')
