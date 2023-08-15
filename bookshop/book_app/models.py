from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class BookAuthor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_author = models.EmailField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email_author}'

    def get_url_author(self):
        return reverse("author-detail", args=[self.id])


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
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    book_info = models.CharField(max_length=100, default='Неизвестно')
    author = models.ForeignKey(BookAuthor, on_delete=models.PROTECT,
                               null=True)  # Добавляем связь многие ко многим / null=True проставляет дефолттные значения

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Book, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f'{self.title} {self.rating}'
