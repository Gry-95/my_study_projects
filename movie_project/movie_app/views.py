from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Movie, Director, Actor


# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/all_movies.html', {
        "movies": movies
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        "movie": movie
    })


def all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors
    })


class DetailDirector(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director


def all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors
    })


class DetailActor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor


class ListMovies(ListView):
    template_name = 'movie_app/list_movies.html'
    model = Movie
    context_object_name = 'directors'
    extra_context = {'actors': Actor.objects.all()}
