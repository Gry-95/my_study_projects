from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Book(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'EURO'),
        (USD, 'DOLLAR'),
        (RUB, 'RUBLIES'),
    ]
    title = models.CharField(max_length=70)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)]
                                 )  # Устанавливаем минимальное и маскимальное значение добавления записи в БД
    is_best_selling = models.BooleanField()
    author = models.CharField(null=True, max_length=100, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Book, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f'{self.title} {self.rating}'
