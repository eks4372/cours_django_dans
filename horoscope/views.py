from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date, timedelta

zodiac_dict = {
    'aries': ['Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).', (3, 21), (4, 20)],
    'taurus': ['Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).', (4, 21), (5, 21)],
    'gemini': ['Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).', (5, 22), (6, 21)],
    'cancer': ['Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).', (6, 22), (7, 21)],
    'leo': ['Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).', (7, 23), (8, 21)],
    'virgo': ['Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).', (8, 22), (9, 23)],
    'libra': ['Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).', (9, 24), (10, 23)],
    'scorpio': ['Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).', (10, 24), (11, 22)],
    'sagittarius': ['Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).', (11, 23), (12, 22)],
    'capricorn': ['Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).', (12, 23), (1, 20)],
    'aquarius': ['Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
                 (1, 21), (2, 19)],
    'pisces': ['Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).', (2, 20), (3, 20)]
}
types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def get_info_about_zodiac(request, zodiac: str):
    description = zodiac_dict.get(zodiac)
    if description:
        # return HttpResponse(f'<h2>{description}</h2>')
        return HttpResponse(f'<h2>{zodiac_dict[zodiac][0]}</h2>')
    else:
        return HttpResponseNotFound(f'<h2>Неизвестный знак зодиака - {zodiac}</h2>')


def get_info_about_zodiac_by_number(request, zodiac: int):
    zodiacs = list(zodiac_dict)
    if zodiac > len(zodiacs):
        return HttpResponseNotFound(f'<h2>Неверный номер знака зодиака - {zodiac}</h2>')
    name_zodiac = zodiacs[zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)  # (f'/horoscope/{name_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    li_element = ''
    for zodiac in zodiacs:
        redirect_path = reverse('horoscope-name', args=(zodiac,))
        li_element += f'<li> <a href="{redirect_path}">{zodiac.title()} </a> </li>'
    response = f'''
    <ol>
        {li_element}
    </ol>
    '''
    return HttpResponse(response)


def get_zodiac_type(request):
    element_type = list(types)
    li_element = ''
    for t in element_type:
        redirect_path = reverse('element-name', args=(t,))
        li_element += f'<li> <a href="{redirect_path}">{t.title()} </a> </li>'
    response = f'''
                <ul>
                    {li_element}
                </ul>
                '''
    return HttpResponse(response)


def get_zodiac_type_elements(request, t: str):
    zodiac_of_element = list(types[t])
    if types.get(t):  # почему то неверный адрес не прилетает суда (
        li_element = ''
        for z in zodiac_of_element:
            redirect_path = reverse('horoscope-name', args=(z,))
            li_element += f'<li> <a href="{redirect_path}">{z.title()} </a> </li>'
        response = f'''
                        <ul>
                            {li_element}
                        </ul>
                        '''
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f'Неверная стихия - {t}')


def get_info_by_date(request, month: int, day: int):
    if 0 < month <= 12 and 0 < day <= (date(2020 + int(month/12), (month+1) % 12, 1)-timedelta(days=1)).day:
        d = date(year=2020, month=month, day=day)
        for i in zodiac_dict:
            y1, y2 = 2020, 2020
            if i == 'capricorn':
                if month == 1:
                    y1 -= 1
                else:
                    y2 += 1
            redirect_url = reverse('horoscope-name', args=(i,))
            d1 = date(year=y1, month=int(zodiac_dict[i][1][0]), day=int(zodiac_dict[i][1][1]))
            d2 = date(year=y2, month=int(zodiac_dict[i][2][0]), day=int(zodiac_dict[i][2][1]))
            if d1 <= d <= d2:
                return HttpResponse(f'<h2>Ваш знак <a href="{redirect_url}">{i}</a></h2>')
    else:
        return HttpResponseNotFound(f'<h2>Невернная дата месяц: {month}, день: {day}</h2>')
