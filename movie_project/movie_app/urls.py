from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('director/', views.all_directors),
    path('director/<int:idt>', views.one_director, name='director-detail'),
    path('actors/', views.all_actors),
    path('actors/<int:actor_id>', views.one_actor, name='actor-detail'),
]
