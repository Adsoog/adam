from datetime import timedelta
from django.utils.timezone import now
from django.db.models import Count
from django.db.models import Count, Sum, F
from cards.models import Cards, Tasks

def get_current_month_range():
    today = now().date()
    first_day_of_month = today.replace(day=1)
    last_day_of_month = (first_day_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    return first_day_of_month, last_day_of_month

def get_total_minutes(user, first_day, last_day):
    tarjetas_mes_actual = Cards.objects.filter(
        user=user,
        date__range=[first_day, last_day]
    )
    total_minutos = sum(tarjeta.total_time for tarjeta in tarjetas_mes_actual)
    return round(total_minutos / 60, 2)

def get_most_frequent_tasks(user, first_day, last_day):
    tarjetas_mes_actual = Cards.objects.filter(
        user=user,
        date__range=[first_day, last_day]
    )
    tareas = Tasks.objects \
        .filter(cardstasksorder__card__in=tarjetas_mes_actual) \
        .annotate(num_veces=Count('cardstasksorder__task')) \
        .annotate(total_minutos=Sum('task_time') * F('num_veces')) \
        .order_by('-num_veces') \
        .values_list('verb', 'object', 'num_veces', 'total_minutos')[:5]

    return [{'verbo': tarea[0], 'objeto': tarea[1], 'num_veces': tarea[2], 'total_horas': round(tarea[3] / 60, 2)} for tarea in tareas]

def get_top_clients_by_time(user, first_day, last_day):
    tarjetas_mes_actual = Cards.objects.filter(
        user=user,
        date__range=[first_day, last_day]
    )

    tareas = Tasks.objects.filter(cardstasksorder__card__in=tarjetas_mes_actual)

    top_clients = tareas.values('client') \
                        .annotate(total_minutos=Sum('task_time')) \
                        .order_by('-total_minutos')[:5]

    return [{'cliente': client['client'], 'total_horas': round(client['total_minutos'] / 60, 2)} for client in top_clients]

def get_hours_by_management_type(user, first_day, last_day):
    tarjetas_mes_actual = Cards.objects.filter(
        user=user,
        date__range=[first_day, last_day]
    )

    tareas = Tasks.objects.filter(cardstasksorder__card__in=tarjetas_mes_actual)

    management_types = tareas.values('measurement') \
                             .annotate(total_minutos=Sum('task_time')) \
                             .order_by('-total_minutos')

    return [{'gestion_tipo': tipo['measurement'], 'total_horas': round(tipo['total_minutos'] / 60, 2)} for tipo in management_types]
