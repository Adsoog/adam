from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import ManoDeObra

class ManoDeObraListView(ListView):
    model = ManoDeObra
    template_name = 'manodeobra/mano_de_obra_list.html'  # Cambia esto cuando tengas las plantillas
    context_object_name = 'mano_de_obra'

class ManoDeObraDetailView(DetailView):
    model = ManoDeObra
    template_name = 'manodeobra/mano_de_obra_detail.html'  # Cambia esto cuando tengas las plantillas

class ManoDeObraCreateView(CreateView):
    model = ManoDeObra
    template_name = 'manodeobra/mano_de_obra_form.html'  # Cambia esto cuando tengas las plantillas
    fields = '__all__'
    success_url = reverse_lazy('mano_de_obra-list')

class ManoDeObraUpdateView(UpdateView):
    model = ManoDeObra
    template_name = 'manodeobra/mano_de_obra_form.html'  # Cambia esto cuando tengas las plantillas
    fields = '__all__'
    success_url = reverse_lazy('mano_de_obra-list')

class ManoDeObraDeleteView(DeleteView):
    model = ManoDeObra
    template_name = 'manodeobra/mano_de_obra_confirm_delete.html'  # Cambia esto cuando tengas las plantillas
    success_url = reverse_lazy('mano_de_obra-list')
