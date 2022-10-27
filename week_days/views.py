from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_info_about_w_days(request, w_day: str):
    if w_day == 'monday':
        return HttpResponse('Список дел на понедельник')
    elif w_day == 'tuesday':
        return HttpResponse('Список дел на вторник')
    else:
        return HttpResponseNotFound(f'Неизвестный день недели - {w_day}')


def get_info_about_w_days_by_number(request, w_day: int):
    if 1 <= w_day <= 7:
        redirect_url = reverse('week_d-name', args=(days[w_day - 1], ))
        return HttpResponseRedirect(redirect_url)  # (f'/todo_week/{days[w_day - 1]}')
    else:
        return HttpResponseNotFound(f'Неверный номер дня недели - {w_day}')
