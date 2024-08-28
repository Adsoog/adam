from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Herramientas

class HerramientasListView(ListView):
    model = Herramientas
    template_name = 'herramientas/herramientas_list.html'  # Cambia esto cuando tengas las plantillas
    context_object_name = 'herramientas'

class HerramientasDetailView(DetailView):
    model = Herramientas
    template_name = 'herramientas/herramientas_detail.html'  # Cambia esto cuando tengas las plantillas

class HerramientasCreateView(CreateView):
    model = Herramientas
    template_name = 'herramientas/herramientas_form.html'  # Cambia esto cuando tengas las plantillas
    fields = '__all__'
    success_url = reverse_lazy('herramientas-list')

class HerramientasUpdateView(UpdateView):
    model = Herramientas
    template_name = 'herramientas/herramientas_form.html'  # Cambia esto cuando tengas las plantillas
    fields = '__all__'
    success_url = reverse_lazy('herramientas-list')

class HerramientasDeleteView(DeleteView):
    model = Herramientas
    template_name = 'herramientas/herramientas_confirm_delete.html'  # Cambia esto cuando tengas las plantillas
    success_url = reverse_lazy('herramientas-list')
