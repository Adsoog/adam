from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Misc

class MiscListView(ListView):
    model = Misc
    template_name = 'misc/misc_list.html' 
    context_object_name = 'misc'

class MiscDetailView(DetailView):
    model = Misc
    template_name = 'misc/misc_detail.html'  

class MiscCreateView(CreateView):
    model = Misc
    template_name = 'misc/misc_form.html'  
    fields = '__all__'
    success_url = reverse_lazy('misc-list')

class MiscUpdateView(UpdateView):
    model = Misc
    template_name = 'misc/misc_form.html' 
    fields = '__all__'
    success_url = reverse_lazy('misc-list')

class MiscDeleteView(DeleteView):
    model = Misc
    template_name = 'misc/misc_confirm_delete.html' 
    success_url = reverse_lazy('misc-list')
