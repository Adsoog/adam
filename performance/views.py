from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from calendar import month_name
from .utils import get_current_month_range, get_total_minutes, get_most_frequent_tasks, get_top_clients_by_time, get_hours_by_management_type
from django.utils.timezone import now

class PerformanceView(LoginRequiredMixin, TemplateView):
    template_name = 'performance.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        first_day_of_month, last_day_of_month = get_current_month_range()
        total_horas_mes = get_total_minutes(usuario, first_day_of_month, last_day_of_month)
        horas_objetivo = 192
        porcentaje_del_objetivo = round((total_horas_mes / horas_objetivo) * 100, 2) if horas_objetivo else 0

        tareas_frecuentes = get_most_frequent_tasks(usuario, first_day_of_month, last_day_of_month)
        top_clients = get_top_clients_by_time(usuario, first_day_of_month, last_day_of_month)
        mes_actual = month_name[now().date().month]
        management_types = get_hours_by_management_type(usuario, first_day_of_month, last_day_of_month)

        context.update({
            'usuario_nombre': usuario.get_full_name() or usuario.username,
            'total_horas_mes': total_horas_mes,
            'porcentaje_del_objetivo': porcentaje_del_objetivo,
            'mes_actual': mes_actual,
            'tareas_frecuentes': tareas_frecuentes,
            'top_clients': top_clients,
            'management_types': management_types
        })

        return context