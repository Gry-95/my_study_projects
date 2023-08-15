from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('director/', views.all_directors),
    path('director/<int:idt>', views.one_director, name='director-detail'),
]
