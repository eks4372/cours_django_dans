from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type', views.get_zodiac_type),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<int:zodiac>', views.get_info_about_zodiac_by_number),
    path('<str:zodiac>', views.get_info_about_zodiac, name='horoscope-name'),
    path('type/<str:t>', views.get_zodiac_type_elements, name='element-name'),
    # path('aries/', views.aries),
    # path('taurus/', views.taurus),
    # path('gemini/', views.gemini),
    # path('cancer/', views.cancer),
    # path('virgo/', views.virgo),
    # path('libra/', views.libra),
    # path('scorpio/', views.scorpio),
    # path('sagittarius/', views.sagittarius),
    # path('capricorn/', views.capricorn),
    # path('aquarius/', views.aquarius),
    # path('pisces/', views.pisces),
]
