from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import math
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника {width}х{height} равна {width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата {width}х{width} равна {width * width}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {math.pi * radius * radius}')


def redirect_to_get_area(request, width: int = 0, height: int = 0, radius: int = 0):
    if not height and not radius:
        redirect_url = reverse('square-name', args=(width,))
        return HttpResponseRedirect(redirect_url)  # (f'/calculate_geometry/square/{width}')
    elif not radius:
        redirect_url = reverse('rectangle-name', args=(width, height))
        return HttpResponseRedirect(redirect_url)  # (f'/calculate_geometry/rectangle/{width}/{height}')
    elif radius:
        redirect_url = reverse('circle-name', args=(radius,))
        return HttpResponseRedirect(redirect_url)  # (f'/calculate_geometry/circle/{radius}')
