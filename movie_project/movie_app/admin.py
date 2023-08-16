from django.contrib import admin
from django.db.models import QuerySet
from django.contrib.auth.models import User
from .models import Movie, Director, Actor, DressingRoom


# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rating', 'year', 'budget', 'director']
    list_editable = ['name', 'rating', 'year']
    prepopulated_fields = {'slug': ('name',)}
    # filter_horizontal = ['actors']  # Добавляет окошко для удобства добавление актеров к фильму
    ordering = ['-rating']  # Сортировка по рейтинку


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    list_editable = ['first_name', 'last_name', 'email']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'gender']
    list_editable = ['first_name', 'last_name', 'gender']


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'floor', 'number']
    list_editable = ['floor', 'number']
