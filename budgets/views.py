from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Budget, BudgetItem
from .forms import BudgetForm, BudgetItemQuantityForm
from inventory.models import EPPS, Equipos, ManoDeObra, Materiales, Misc, Herramientas, Transporte, Consumibles, Alimentos
from .utils import export_budget_report_to_excel 
from django.contrib.contenttypes.models import ContentType
from collections import defaultdict
from django.db import transaction

class BudgetListView(ListView):
    model = Budget
    template_name = 'budgets/budget_list.html'
    context_object_name = 'budgets'

class BudgetDetailView(DetailView):
    model = Budget
    template_name = 'budgets/budget_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipos'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'EQUIPOS']
        context['epps'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'EPPS']
        context['transporte'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'TRANSPORTE']
        context['materiales'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'MATERIALES']
        context['consumibles'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'CONSUMIBLES']
        context['alimentos'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'ALIMENTOS']
        context['manodeobra'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'MANODEOBRA']
        context['herramientas'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'HERRAMIENTAS']
        context['misc'] = [item for item in self.object.items.all() if item.inventario.grupo_articulos == 'MISC']
        context['export_url'] = reverse_lazy('budget-export', kwargs={'pk': self.object.pk})
        return context

    
class BudgetCreateView(CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budgets/budget_form.html'
    success_url = reverse_lazy('budget-list')

    def get_success_url(self):
        return reverse_lazy('budget-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save()
        inventarios_list = [
            form.cleaned_data.get('inventarios_equipos', []),
            form.cleaned_data.get('inventarios_epps', []),
            form.cleaned_data.get('inventarios_transporte', []),
            form.cleaned_data.get('inventarios_materiales', []),
            form.cleaned_data.get('inventarios_consumibles', []),
            form.cleaned_data.get('inventarios_alimentos', []),
            form.cleaned_data.get('inventarios_manodeobra', []),
            form.cleaned_data.get('inventarios_herramientas', []),
            form.cleaned_data.get('inventarios_misc', [])
        ]
        for inventarios in inventarios_list:
            for inventario in inventarios:
                BudgetItem.objects.create(
                    budget=self.object,
                    content_type=ContentType.objects.get_for_model(inventario),
                    object_id=inventario.id,
                    cantidad=1
                )
        self.object.calcular_valor_total()
        return redirect(self.get_success_url())

from django.db import transaction

class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budgets/budget_form.html'

    def get_success_url(self):
        return reverse_lazy('budget-detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        initial = super().get_initial()
        initial['inventarios_equipos'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(Equipos)).values_list('object_id', flat=True)
        initial['inventarios_epps'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(EPPS)).values_list('object_id', flat=True)
        initial['inventarios_transporte'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(Transporte)).values_list('object_id', flat=True)
        initial['inventarios_materiales'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(Materiales)).values_list('object_id', flat=True)
        initial['inventarios_consumibles'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(Consumibles)).values_list('object_id', flat=True)
        initial['inventarios_alimentos'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(Alimentos)).values_list('object_id', flat=True)
        initial['inventarios_manodeobra'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(ManoDeObra)).values_list('object_id', flat=True)
        initial['inventarios_herramientas'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(Herramientas)).values_list('object_id', flat=True)
        initial['inventarios_misc'] = self.object.items.filter(content_type=ContentType.objects.get_for_model(Misc)).values_list('object_id', flat=True)
        return initial

    @transaction.atomic
    def form_valid(self, form):
        budget = form.save(commit=False)  # Guardar sin guardar en la base de datos aún

        # Mapeo de inventarios en el formulario a sus respectivos modelos
        inventarios_map = {
            'inventarios_equipos': Equipos,
            'inventarios_epps': EPPS,
            'inventarios_transporte': Transporte,
            'inventarios_materiales': Materiales,
            'inventarios_consumibles': Consumibles,
            'inventarios_alimentos': Alimentos,
            'inventarios_manodeobra': ManoDeObra,
            'inventarios_herramientas': Herramientas,
            'inventarios_misc': Misc,
        }

        # Lista para almacenar los PKs de los inventarios seleccionados en el formulario
        new_inventarios_pks = []

        # Procesar la selección de ítems
        for field_name, model_class in inventarios_map.items():
            selected_inventarios = form.cleaned_data.get(field_name, [])
            for inventario in selected_inventarios:
                new_inventarios_pks.append(inventario.pk)
                # Si no existe ya, crea la relación BudgetItem
                BudgetItem.objects.get_or_create(
                    budget=budget,
                    content_type=ContentType.objects.get_for_model(model_class),
                    object_id=inventario.id,
                    defaults={'cantidad': 1}  # Aquí podrías personalizar la cantidad si es necesario
                )

        # Eliminar las relaciones no seleccionadas
        items_to_delete = budget.items.exclude(object_id__in=new_inventarios_pks)
        items_to_delete.delete()

        # Guardar el objeto budget para persistir los cambios
        budget.save()

        # Recalcular el valor total del presupuesto y guardar nuevamente
        budget.calcular_valor_total()
        budget.save(update_fields=[
            'total_soles_parcial', 'total_dolares_parcial',
            'total_soles_final', 'total_dolares_final',
            'total_utilidad', 'total_gastos_administrativos'
        ])

        return redirect(self.get_success_url())




class BudgetItemUpdateView(UpdateView):
    model = Budget
    template_name = 'budgets/budget_item_update_form.html'
    fields = []  # Esto resuelve el problema, pero no se usa realmente en la vista

    def get_success_url(self):
        return reverse_lazy('budget-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = BudgetItem.objects.filter(budget=self.object)
        context['item_forms'] = [
            BudgetItemQuantityForm(instance=item, prefix=str(item.pk)) for item in context['items']
        ]
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        items = BudgetItem.objects.filter(budget=self.object)
        is_valid = True
        item_forms = []

        for item in items:
            item_form = BudgetItemQuantityForm(request.POST, instance=item, prefix=str(item.pk))
            item_forms.append(item_form)
            if item_form.is_valid():
                item_form.save()
            else:
                is_valid = False

        self.object.calcular_valor_total()

        if is_valid:
            return redirect(self.get_success_url())
        else:
            context = self.get_context_data(item_forms=item_forms)
            return self.render_to_response(context)

    def form_invalid(self, form):
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'budgets/budget_confirm_delete.html'
    success_url = reverse_lazy('budget-list')

def export_budget_report(request, pk):
    return export_budget_report_to_excel(request, pk)
