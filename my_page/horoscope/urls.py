from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type', views.type),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('type/<str:sign_element>', views.type_element, name="type-name"),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:month>/<int:day>', views.horoscope_dates),
    path('<int:sign_zodiac>', views.change_zodiac_num),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
