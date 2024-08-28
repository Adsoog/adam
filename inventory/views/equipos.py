from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Equipos

class EquiposListView(ListView):
    model = Equipos
    template_name = 'equipo/equipos_list.html'
    context_object_name = 'equipos'

class EquiposDetailView(DetailView):
    model = Equipos
    template_name = 'equipo/equipos_detail.html'

class EquiposCreateView(CreateView):
    model = Equipos
    template_name = 'equipo/equipos_form.html'
    fields = '__all__'
    success_url = reverse_lazy('equipos-list')

class EquiposUpdateView(UpdateView):
    model = Equipos
    template_name = 'equipo/equipos_form.html'
    fields = '__all__'
    success_url = reverse_lazy('equipos-list')

class EquiposDeleteView(DeleteView):
    model = Equipos
    template_name = 'equipo/equipos_confirm_delete.html'
    success_url = reverse_lazy('equipos-list')
