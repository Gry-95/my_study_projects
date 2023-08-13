from django.contrib import admin
from django.db.models import QuerySet
from django.contrib.auth.models import User
from .models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'is_best_selling', 'currency', 'author', 'slug', 'rating_status'] #Добавление полей в админку
    list_editable = ['rating', 'currency','is_best_selling', 'author'] #редактирование поля
    list_per_page = 15
    ordering = ['-rating']
    actions = ['set_dollars', 'set_euro']
    search_fields = ['title']

    @admin.display(ordering='rating', description='Статус') #Добавляет колонку статус
    def rating_status(self, book: Book):
        if book.rating < 70:
            return 'Не стоит внимания'
        if book.rating < 80:
            return 'На разок почитать'
        return 'Стоит прочитать'

    @admin.action(description='Валюту в доллар')
    def set_dollars(self, request, qs: QuerySet): #Проставляет в колонке currency Dollars
        qs.update(currency=Book.USD)

    @admin.action(description='Валюту в Евро')
    def set_euro(self, request, qs: QuerySet):  # Проставляет в колонке currency Euro
        count_updated = qs.update(currency=Book.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} значений')



#admin.site.register(Book, BookAdmin) - Вместо декоратора
