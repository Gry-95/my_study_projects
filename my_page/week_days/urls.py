from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('<int:day_week>', views.num_day),
    path('<str:day_week>', views.week_day, name='day-of-week'),
]
