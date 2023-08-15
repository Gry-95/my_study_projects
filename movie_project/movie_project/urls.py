from django.contrib import admin
from django.urls import path,include
from movie_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),
    path('movie/<str:slug_movie>', views.show_one_movie, name='movie-detail'),
]
