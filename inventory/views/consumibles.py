from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Consumibles

class ConsumiblesListView(ListView):
    model = Consumibles
    template_name = 'consumibles/consumibles_list.html'
    context_object_name = 'consumibles'

class ConsumiblesDetailView(DetailView):
    model = Consumibles
    template_name = 'consumibles/consumibles_detail.html'

class ConsumiblesCreateView(CreateView):
    model = Consumibles
    template_name = 'consumibles/consumibles_form.html'
    fields = '__all__'
    success_url = reverse_lazy('consumibles-list')

class ConsumiblesUpdateView(UpdateView):
    model = Consumibles
    template_name = 'consumibles/consumibles_form.html'
    fields = '__all__'
    success_url = reverse_lazy('consumibles-list')

class ConsumiblesDeleteView(DeleteView):
    model = Consumibles
    template_name = 'consumibles/consumibles_confirm_delete.html'
    success_url = reverse_lazy('consumibles-list')
