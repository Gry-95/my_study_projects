from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.CharField(null=True, max_length=100)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Book, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f'{self.title} {self.rating}'
