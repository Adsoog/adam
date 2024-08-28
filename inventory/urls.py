from django.urls import path
from .views.inventario import InventarioListView, upload_file_view
from .views.equipos import EquiposListView, EquiposDetailView, EquiposCreateView, EquiposUpdateView, EquiposDeleteView
from .views.alimentos import AlimentosListView, AlimentosDetailView, AlimentosCreateView, AlimentosUpdateView, AlimentosDeleteView
from .views.consumibles import ConsumiblesListView, ConsumiblesDetailView, ConsumiblesCreateView, ConsumiblesUpdateView, ConsumiblesDeleteView
from .views.epps import EPPSListView, EPPSDetailView, EPPSCreateView, EPPSUpdateView, EPPSDeleteView
from .views.herramientas import HerramientasListView, HerramientasDetailView, HerramientasCreateView, HerramientasUpdateView, HerramientasDeleteView
from .views.mano_de_obra import ManoDeObraListView, ManoDeObraDetailView, ManoDeObraCreateView, ManoDeObraUpdateView, ManoDeObraDeleteView
from .views.materiales import MaterialesListView, MaterialesDetailView, MaterialesCreateView, MaterialesUpdateView, MaterialesDeleteView
from .views.misc import MiscListView, MiscDetailView, MiscCreateView, MiscUpdateView, MiscDeleteView
from .views.transporte import TransporteListView, TransporteDetailView, TransporteCreateView, TransporteUpdateView, TransporteDeleteView

urlpatterns = [
    path('inventario/', InventarioListView.as_view(), name='inventario_list'),
    path('upload-excel/', upload_file_view, name='upload_excel'),
    
    #EQUIPOS
    path('inventario/equipos/', EquiposListView.as_view(), name='equipos-list'),
    path('inventario/equipos/<int:pk>/', EquiposDetailView.as_view(), name='equipos-detail'),
    path('inventario/equipos/nuevo/', EquiposCreateView.as_view(), name='equipos-create'),
    path('inventario/equipos/<int:pk>/editar/', EquiposUpdateView.as_view(), name='equipos-update'),
    path('inventario/equipos/<int:pk>/eliminar/', EquiposDeleteView.as_view(), name='equipos-delete'),
    
    #ALIMENTOS
    path('inventario/alimentos/', AlimentosListView.as_view(), name='alimentos-list'),
    path('inventario/alimentos/<int:pk>/', AlimentosDetailView.as_view(), name='alimentos-detail'),
    path('inventario/alimentos/nuevo/', AlimentosCreateView.as_view(), name='alimentos-create'),
    path('inventario/alimentos/<int:pk>/editar/', AlimentosUpdateView.as_view(), name='alimentos-update'),
    path('inventario/alimentos/<int:pk>/eliminar/', AlimentosDeleteView.as_view(), name='alimentos-delete'),

    #CONSUMIBLES
    path('inventario/consumibles/', ConsumiblesListView.as_view(), name='consumibles-list'),
    path('inventario/consumibles/<int:pk>/', ConsumiblesDetailView.as_view(), name='consumibles-detail'),
    path('inventario/consumibles/nuevo/', ConsumiblesCreateView.as_view(), name='consumibles-create'),
    path('inventario/consumibles/<int:pk>/editar/', ConsumiblesUpdateView.as_view(), name='consumibles-update'),
    path('inventario/consumibles/<int:pk>/eliminar/', ConsumiblesDeleteView.as_view(), name='consumibles-delete'),
    
    #EPPS
    path('inventario/epps/', EPPSListView.as_view(), name='epps-list'),
    path('inventario/epps/<int:pk>/', EPPSDetailView.as_view(), name='epps-detail'),
    path('inventario/epps/nuevo/', EPPSCreateView.as_view(), name='epps-create'),
    path('inventario/epps/<int:pk>/editar/', EPPSUpdateView.as_view(), name='epps-update'),
    path('inventario/epps/<int:pk>/eliminar/', EPPSDeleteView.as_view(), name='epps-delete'),

    #HERRAMIENTAS
    path('inventario/herramientas/', HerramientasListView.as_view(), name='herramientas-list'),
    path('inventario/herramientas/<int:pk>/', HerramientasDetailView.as_view(), name='herramientas-detail'),
    path('inventario/herramientas/nuevo/', HerramientasCreateView.as_view(), name='herramientas-create'),
    path('inventario/herramientas/<int:pk>/editar/', HerramientasUpdateView.as_view(), name='herramientas-update'),
    path('inventario/herramientas/<int:pk>/eliminar/', HerramientasDeleteView.as_view(), name='herramientas-delete'),
    
    #MANO DE OBRA
    path('inventario/mano_de_obra/', ManoDeObraListView.as_view(), name='mano_de_obra-list'),
    path('inventario/mano_de_obra/<int:pk>/', ManoDeObraDetailView.as_view(), name='mano_de_obra-detail'),
    path('inventario/mano_de_obra/nuevo/', ManoDeObraCreateView.as_view(), name='mano_de_obra-create'),
    path('inventario/mano_de_obra/<int:pk>/editar/', ManoDeObraUpdateView.as_view(), name='mano_de_obra-update'),
    path('inventario/mano_de_obra/<int:pk>/eliminar/', ManoDeObraDeleteView.as_view(), name='mano_de_obra-delete'),

    #MATERIALES
    path('inventario/materiales/', MaterialesListView.as_view(), name='materiales-list'),
    path('inventario/materiales/<int:pk>/', MaterialesDetailView.as_view(), name='materiales-detail'),
    path('inventario/materiales/nuevo/', MaterialesCreateView.as_view(), name='materiales-create'),
    path('inventario/materiales/<int:pk>/editar/', MaterialesUpdateView.as_view(), name='materiales-update'),
    path('inventario/materiales/<int:pk>/eliminar/', MaterialesDeleteView.as_view(), name='materiales-delete'),
    
    #MISC
    path('inventario/misc/', MiscListView.as_view(), name='misc-list'),
    path('inventario/misc/<int:pk>/', MiscDetailView.as_view(), name='misc-detail'),
    path('inventario/misc/nuevo/', MiscCreateView.as_view(), name='misc-create'),
    path('inventario/misc/<int:pk>/editar/', MiscUpdateView.as_view(), name='misc-update'),
    path('inventario/misc/<int:pk>/eliminar/', MiscDeleteView.as_view(), name='misc-delete'),
    
    #TRASNPORTE
    path('inventario/transporte/', TransporteListView.as_view(), name='transporte-list'),
    path('inventario/transporte/<int:pk>/', TransporteDetailView.as_view(), name='transporte-detail'),
    path('inventario/transporte/nuevo/', TransporteCreateView.as_view(), name='transporte-create'),
    path('inventario/transporte/<int:pk>/editar/', TransporteUpdateView.as_view(), name='transporte-update'),
    path('inventario/transporte/<int:pk>/eliminar/', TransporteDeleteView.as_view(), name='transporte-delete'),

]