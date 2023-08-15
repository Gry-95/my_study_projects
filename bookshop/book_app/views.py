from django.shortcuts import render, get_object_or_404
from .models import Book, BookAuthor
from django.db.models import F, Avg, Min, Max, Count, Value

# Create your views here.
def show_all_books(request):
    books = Book.objects.order_by(F('is_best_selling').desc()) # Соритровка по лучшим продажам
    # books = Book.objects.annotate(
    # new_columm = (
    # F('rating') + 100,
    # )           #Отображает новые колонки в дебаг тулбаре. НЕ ВНОСИТ ИЗМЕНЕНИЯ В БД!
    agg = books.aggregate(Avg('rating'), Min('rating'), Max('rating'), Count('id'))
    return render(request, 'book_app/all_books.html', {
        "books": books,
        'agg': agg,
    })

def show_authors(request):
    authors = BookAuthor.objects.all()
    return render(request, 'book_app/all_authors.html', {
        "authors": authors,
    })

def show_author(request, id_author:int):
    author = get_object_or_404(BookAuthor, id=id_author)
    return render(request, 'book_app/one_author.html', {
        "author": author
    })

def show_one_book(request, slug_book:str):
    book = get_object_or_404(Book, slug=slug_book)
    return render(request, 'book_app/one_book.html', {
        "book": book
    })