from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from ..models import Equipos, EPPS, Transporte, Materiales, Consumibles, Alimentos, ManoDeObra, Herramientas, Misc
from django.views.generic import TemplateView

class InventarioListView(TemplateView):
    template_name = 'inventario/inventario_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipos_count'] = Equipos.objects.count()
        context['epps_count'] = EPPS.objects.count()
        context['transporte_count'] = Transporte.objects.count()
        context['materiales_count'] = Materiales.objects.count()
        context['consumibles_count'] = Consumibles.objects.count()
        context['alimentos_count'] = Alimentos.objects.count()
        context['mano_de_obra_count'] = ManoDeObra.objects.count()
        context['herramientas_count'] = Herramientas.objects.count()
        context['misc_count'] = Misc.objects.count()
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
            
            # Verificar los nombres de las columnas
            expected_columns = [
                'Núm. Artículo', 'Descripción', 'Stock', 'Cód. Barras', 'Grupo', 
                'Fabricante', 'Unidad de Medida', 'Última Reval.', 'Último Precio'
            ]
            if not all(column in data.columns for column in expected_columns):
                ignored_sheets.append(sheet_name)
                continue
            
            # Normalizar los nombres de las columnas
            data.columns = data.columns.str.strip()
            
            # Rellenar NaN con valores predeterminados
            data['Última Reval.'] = data['Última Reval.'].fillna(0)
            data['Último Precio'] = data['Último Precio'].fillna(0)
            
            model_class = get_model_for_sheet(sheet_name)  # Obtener el modelo correspondiente al nombre de la hoja

            if model_class:
                # Procesar cada fila del DataFrame
                for index, row in data.iterrows():
                    instance = model_class(
                        num_articulo=row['Núm. Artículo'],
                        descripcion=row['Descripción'],
                        en_stock=row['Stock'],
                        codigo_barras=row['Cód. Barras'],
                        grupo_articulos=row['Grupo'],
                        fabricante=row['Fabricante'],
                        unidad_medida=row['Unidad de Medida'],
                        precio_unitario_diario=row['Última Reval.'],  # Asegurar que el nombre de la columna es correcto
                        ultimo_precio_compra=row['Último Precio']
                    )
                    instance.save()
            else:
                ignored_sheets.append(sheet_name)  # Añadir el nombre de la hoja ignorada a la lista

        if ignored_sheets:
            message = f"Archivo procesado con éxito, pero se ignoraron las hojas: {', '.join(ignored_sheets)}"
        else:
            message = "Archivo procesado con éxito"

        return HttpResponse(message)

    return render(request, 'inventario/upload_excel.html')

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
