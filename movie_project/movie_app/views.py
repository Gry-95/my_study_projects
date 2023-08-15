from django.shortcuts import render, get_object_or_404
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


def one_director(request, idt):
    director = get_object_or_404(Director, id=idt)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })


def all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors
    })


def one_actor(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor
    })
