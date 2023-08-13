from django.contrib import admin
from django.db.models import QuerySet
from django.contrib.auth.models import User
from .models import Book


# Register your models here.
class Rating_filter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Рейтинг низкий'),
            ('от 40 до 59', 'Рейтинг средний'),
            ('от 60 до 79', 'Рейтинг высокий'),
            ('>=80', 'Рейтинг максимальный')
        ]

    def queryset(self, request, queryset: QuerySet):  # Добавляем в фильтр разделение по рейтингу
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gt=39, rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gt=59, rating__lt=80)
        return queryset.filter(rating__gt=79)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'rating'] #В добавление элемента в ДБ указываем поля для заполнения
    exclude = ['slug']  # Выбираем поля которые исключим из добавления в БД
    list_display = ['title', 'rating', 'is_best_selling', 'currency', 'author', 'slug',
                    'rating_status']  # Добавление полей в админку
    prepopulated_fields = {
        'slug': (
            'name',
        )}  # Указываем что поле slug предвычисляемое и оно будет заполняться автоматичски на основе введенного имени
    readonly_fields = ['author']  # Выбираем поля которые пользватель не сможет редактивровать
    list_editable = ['rating', 'currency', 'is_best_selling', 'author']  # редактирование поля
    list_per_page = 15  # Указываем сколько записей помещается на странице
    ordering = ['-rating']  # Сортировка по рейтингу
    actions = ['set_dollars', 'set_euro']  # Добавили возможность изменять валюту выбранным элементам БД
    search_fields = ['title']  # Добавляем в поиск поля для поиска (по которым будем искать)
    list_filter = ['title', Rating_filter]  # Добавляем в фильтр данные

    @admin.display(ordering='rating', description='Статус')  # Добавляет колонку статус
    def rating_status(self, book: Book):
        if book.rating < 70:
            return 'Не стоит внимания'
        if book.rating < 80:
            return 'На разок почитать'
        return 'Стоит прочитать'

    @admin.action(description='Валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):  # Проставляет в колонке currency Dollars
        qs.update(currency=Book.USD)

    @admin.action(description='Валюту в Евро')
    def set_euro(self, request, qs: QuerySet):  # Проставляет в колонке currency Euro
        count_updated = qs.update(currency=Book.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} значений')

# admin.site.register(Book, BookAdmin) - Вместо декоратора
