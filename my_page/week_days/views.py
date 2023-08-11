from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

DAYS = {
    'monday': 'Понедельник',
    'tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'thursday': 'Четверг',
    'friday': 'Пятница',
    'saturday': 'Суббота',
    'sunday': 'Воскресенье'
}


def main_page(request):
    return render(request, 'week_days/greeting.html')


def week_day(request, day_week):
    if day_week in DAYS:
        return HttpResponse(DAYS[day_week])
    else:
        return HttpResponseNotFound('Такого дня неделе не существует')


def num_day(request, day_week):
    if 1 <= day_week <= 7:
        days_log = list(DAYS)[day_week - 1]
        day_redirect_url = reverse('day-of-week', args=(days_log,))
        return HttpResponseRedirect(day_redirect_url)
    return HttpResponse(f'Неверный номер дня - {day_week}')
