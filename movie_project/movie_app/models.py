from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def get_url_dir(self):
        return reverse('director-detail', args=[self.id])


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.floor} {self.number}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер - {self.first_name} {self.last_name}'
        else:
            return f'Актриса - {self.first_name} {self.last_name}'

    def get_url_act(self):
        return reverse('actor-detail', args=[self.id])


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)  # дб индекс для быстрого поиска при расширении бд
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):  # Сохраняю слаг, хавает ру символы
        self.slug = slugify(self.name, allow_unicode=True)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):  # Генерирую url
        return reverse("movie-detail", args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
