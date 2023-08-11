from django.urls import path
from movie_app import views

urlpatterns = [
    path('', views.show_all_movie),
]
