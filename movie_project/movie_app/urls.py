from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('director/', views.all_directors),
    path('director/<int:pk>', views.DetailDirector.as_view(), name='director-detail'),
    path('actors/', views.all_actors),
    path('actors/<int:pk>', views.DetailActor.as_view(), name='actor-detail'),
    path('list', views.ListMovies.as_view())
]
