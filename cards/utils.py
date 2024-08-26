from django.db.models import Max
from .models import CardsTasksOrder


def get_max_order(card) -> int:
    existing_tasks = CardsTasksOrder.objects.filter(card=card)
    if not existing_tasks.exists():
        return 1
    else:
        current_max = existing_tasks.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1
