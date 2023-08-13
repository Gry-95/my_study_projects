from django.db import models
from django.urls import reverse
from django.utils.text import slugify #слагифай хавает ру символы


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True) #дб индекс для быстрого поиска при расширении бд

    def save(self, *args, **kwargs): #Сохраняю слаг, хавает ру символы
        self.slug = slugify(self.name, allow_unicode=True)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self): #Генерирую url
        return reverse("movie-detail", args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
