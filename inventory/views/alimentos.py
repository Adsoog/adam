from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Alimentos

class AlimentosListView(ListView):
    model = Alimentos
    template_name = 'alimentos/alimentos_list.html'
    context_object_name = 'alimentos'

class AlimentosDetailView(DetailView):
    model = Alimentos
    template_name = 'alimentos/alimentos_detail.html'

class AlimentosCreateView(CreateView):
    model = Alimentos
    template_name = 'alimentos/alimentos_form.html'
    fields = '__all__'
    success_url = reverse_lazy('alimentos-list')

class AlimentosUpdateView(UpdateView):
    model = Alimentos
    template_name = 'alimentos/alimentos_form.html'
    fields = '__all__'
    success_url = reverse_lazy('alimentos-list')

class AlimentosDeleteView(DeleteView):
    model = Alimentos
    template_name = 'alimentos/alimentos_confirm_delete.html'
    success_url = reverse_lazy('alimentos-list')
