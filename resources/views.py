from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import AssignResourceForm, ResourceForm, HazardForm
from .models import Hazard, Risk, Cause, Control, Resource

class CombinedFormView(TemplateView):
    template_name = 'resources/combined_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seguridad_resources'] = Resource.objects.filter(resource_type='seguridad').prefetch_related('hazards')
        context['calidad_resources'] = Resource.objects.filter(resource_type='calidad').prefetch_related('hazards')
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update({
            'resource_form': ResourceForm(prefix='resource'),
            'hazard_form': HazardForm(prefix='hazard'),
        })
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if 'form_type' in request.POST and request.POST['form_type'] == 'resource_form':
            resource_form = ResourceForm(request.POST, prefix='resource')
            if resource_form.is_valid():
                resource_form.save()
                return redirect('create-resource-hazard')
        elif 'form_type' in request.POST and request.POST['form_type'] == 'hazard_form':
            hazard_form = HazardForm(request.POST, prefix='hazard')
            if hazard_form.is_valid():
                hazard = hazard_form.save(commit=False)
                hazard.save()  # Primero guarda el Hazard
                hazard_form.save_m2m()  # Guarda las relaciones ManyToMany

                # Crear y asociar Risk, Cause y Control
                risk_description = hazard_form.cleaned_data['risk_description']
                if risk_description:
                    Risk.objects.create(hazard=hazard, description=risk_description)

                cause_description = hazard_form.cleaned_data['cause_description']
                if cause_description:
                    Cause.objects.create(hazard=hazard, description=cause_description)

                control_measures = hazard_form.cleaned_data['control_measures']
                if control_measures:
                    Control.objects.create(hazard=hazard, measures=control_measures)

                return redirect('create-resource-hazard')

        # Si el formulario no es válido o si no es un POST de form, renderiza el form nuevamente
        context.update({
            'resource_form': ResourceForm(prefix='resource'),
            'hazard_form': HazardForm(prefix='hazard'),
        })
        return render(request, self.template_name, context)

def assign_resource(request, tarea_id):
    pass

    # tarea = NewTarea.objects.get(pk=tarea_id)
    # resources = Resource.objects.all()

    # if request.method == 'POST':
    #     form = AssignResourceForm(request.POST)
    #     if form.is_valid():
    #         selected_resources = form.cleaned_data['resources']
    #         tarea.resources.set(selected_resources)
    #         return redirect('new_lista_tareas')
    # else:
    #     form = AssignResourceForm()

    # context = {'tarea': tarea, 'form': form, 'resources': resources}
    # return render(request, 'resources/add_recurso.html', context)