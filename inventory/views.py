from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Equipos, EPPS, Transporte, Materiales, Consumibles, Alimentos, ManoDeObra, Herramientas, Misc
from django.views.generic import ListView, TemplateView
from django.db.models import Q
import pandas as pd
from django.http import HttpResponse

class InventarioListView(TemplateView):
    template_name = 'inventario/inventario_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipos'] = Equipos.objects.all()
        context['epps'] = EPPS.objects.all()
        context['transporte'] = Transporte.objects.all()
        context['materiales'] = Materiales.objects.all()
        context['consumibles'] = Consumibles.objects.all()
        context['alimentos'] = Alimentos.objects.all()
        context['mano_de_obra'] = ManoDeObra.objects.all()
        context['herramientas'] = Herramientas.objects.all()
        context['misc'] = Misc.objects.all()
        return context

def upload_file_view(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        
        # Cargar todas las hojas del archivo Excel
        xls = pd.ExcelFile(excel_file)
        sheets = xls.sheet_names
        
        ignored_sheets = []  # Lista para mantener registro de las hojas ignoradas
        
        for sheet_name in sheets:
            data = pd.read_excel(xls, sheet_name)
            model_class = get_model_for_sheet(sheet_name)  # Obtener el modelo correspondiente al nombre de la hoja

            if model_class:
                # Procesar cada fila del DataFrame
                for index, row in data.iterrows():
                    instance = model_class(
                        num_articulo=row['num_articulo'],
                        descripcion=row['descripcion'],
                        en_stock=row['en_stock'],
                        codigo_barras=row['codigo_barras'],
                        fabricante=row['fabricante'],
                        unidad_medida=row['unidad_medida'],
                        precio_unitario_diario=row.get('precio_unitario_diario', 0),
                        ultimo_precio_compra=row.get('ultimo_precio_compra', 0)
                    )
                    instance.save()
            else:
                ignored_sheets.append(sheet_name)  # Añadir el nombre de la hoja ignorada a la lista

        if ignored_sheets:
            message = f"Archivo procesado con éxito, pero se ignoraron las hojas: {', '.join(ignored_sheets)}"
        else:
            message = "Archivo procesado con éxito"

        return HttpResponse(message)

    return render(request, 'inventario/upload.html')

def get_model_for_sheet(sheet_name):
    mapping = {
        'EQUIPOS': Equipos,
        'EPPS': EPPS,
        'TRANSPORTE': Transporte,
        'MATERIALES': Materiales,
        'CONSUMIBLES': Consumibles,
        'ALIMENTOS': Alimentos,
        'MANO DE OBRA': ManoDeObra,
        'HERRAMIENTAS': Herramientas,
        'MISC': Misc
    }
    return mapping.get(sheet_name.strip().upper(), None)
