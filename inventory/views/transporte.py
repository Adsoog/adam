from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Transporte

class TransporteListView(ListView):
    model = Transporte
    template_name = 'trasnportes/transporte_list.html'  # Cambia esto cuando tengas las plantillas
    context_object_name = 'transporte'

class TransporteDetailView(DetailView):
    model = Transporte
    template_name = 'trasnportes/transporte_detail.html'  # Cambia esto cuando tengas las plantillas

class TransporteCreateView(CreateView):
    model = Transporte
    template_name = 'trasnportes/transporte_form.html'  # Cambia esto cuando tengas las plantillas
    fields = '__all__'
    success_url = reverse_lazy('transporte-list')

class TransporteUpdateView(UpdateView):
    model = Transporte
    template_name = 'trasnportes/transporte_form.html'  # Cambia esto cuando tengas las plantillas
    fields = '__all__'
    success_url = reverse_lazy('transporte-list')

class TransporteDeleteView(DeleteView):
    model = Transporte
    template_name = 'trasnportes/transporte_confirm_delete.html'  # Cambia esto cuando tengas las plantillas
    success_url = reverse_lazy('transporte-list')
