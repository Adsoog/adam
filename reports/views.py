# views.py
from datetime import date, timedelta, datetime
from django.shortcuts import render
from .utils import get_daily_valuations_for_month
from datetime import date
from cards.models import Cards
from collections import defaultdict
from django.http import JsonResponse

def valuations_view(request, year, month):
    raw_valuations = get_daily_valuations_for_month(year, month)
    num_days = (datetime(year, month + 1, 1) - datetime(year, month, 1)).days
    days = list(range(1, num_days + 1))

    # Simplifica la preparación de los datos
    valuations = []
    for user, days_valuations in raw_valuations.items():
        row = [user] + [days_valuations.get(day, '-') for day in days]
        valuations.append(row)

    return render(request, 'valuations_list.html', {
        'valuations': valuations,
        'days': days
    })