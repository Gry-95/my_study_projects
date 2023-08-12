from django.urls import path
from movie_app import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<str:slug_movie>', views.show_one_movie, name='movie-detail'),
]
