from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

# # Create your views here.
ZODIAC = {
    "aries": "Овен - первый знак зодиака, "
             "планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, "
              "планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, "
              "планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, "
              "Луна (с 22 июня по 22 июля).",
    'leo': ' Лев - пятый знак зодиака, '
           'солнце (с 23 июля по 21 августа).',
    "virgo": "Дева - шестой знак зодиака, "
             "планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, "
             "планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, "
               "планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, "
                   "планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, "
                 "планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, "
                "планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, "
              "планеты Юпитер (с 20 февраля по 20 марта)."
}
ZODIAC_DATES = {
    "aries": (3, 21, 4, 20),
    "taurus": (4, 21, 5, 21),
    "gemini": (5, 22, 6, 21),
    "cancer": (6, 22, 7, 22),
    "leo": (7, 23, 8, 21),
    "virgo": (8, 22, 9, 23),
    "libra": (9, 24, 10, 23),
    "scorpio": (10, 24, 11, 22),
    "sagittarius": (11, 23, 12, 22),
    "capricorn": (12, 23, 1, 20),
    "aquarius": (1, 21, 2, 19),
    "pisces": (2, 20, 3, 20)}

ZODIAC_TYPES = {'fire': ['aries', 'leo', 'sagittarius'],
                'earth': ['taurus', 'virgo', 'capricorn'],
                'air': ['gemini', 'libra', 'aquarius'],
                'water': ['cancer', 'scorpio', 'pisces']}


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def horoscope_dates(request, month, day):
    for monthes, days in ZODIAC_DATES.items():
        if days[0] == month and day >= days[1] or days[2] == month and day <= days[3]:
            return HttpResponse(ZODIAC[monthes])
    else:
        return HttpResponse(f'Введена некорректная дата: месяц - {month}, день - {day}')


def index(request):
    zodiacs = list(ZODIAC)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


def type(request):
    elements = ''
    for sign in ZODIAC_TYPES:
        elements_url = reverse('type-name', args=[sign])
        elements += f'<li> <a href="{elements_url}">{sign.title()}</a> </li>'
    response = f"""<ul>{elements}</ul>"""
    return HttpResponse(response)


def type_element(request, sign_element):
    response = ZODIAC_TYPES[sign_element]
    elements = ''
    for sign in response:
        elements_url = reverse('horoscope-name', args=[sign])
        elements += f'<li> <a href="{elements_url}">{sign.title()}</a> </li>'
    response = f"""<ul>{elements}</ul>"""
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac):
    if sign_zodiac in ZODIAC:
        description = ZODIAC[sign_zodiac]
        data = {
            'description_zodiac': description,
            'sign': sign_zodiac.title(),
        }
        return render(request, 'horoscope/info_zodiac.html', context=data)
    else:
        data = {
            'description_zodiac': None,
            'sign': sign_zodiac.title(),
        }
        return render(request, 'horoscope/info_zodiac.html', context=data)


def change_zodiac_num(request, sign_zodiac):
    zodiacs = list(ZODIAC)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def some_table(request):
    return render(request, 'beautiful_table/beautiful_table.html' )