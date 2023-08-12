from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import F, Avg, Min, Max, Count

# Create your views here.
def show_all_books(request):
    books = Book.objects.order_by(F('is_best_selling').desc())
    agg = books.aggregate(Avg('rating'), Min('rating'), Max('rating'), Count('id'))
    return render(request, 'book_app/all_books.html', {
        "books": books,
        'agg': agg,
    })


def show_one_book(request, slug_book:str):
    book = get_object_or_404(Book, slug=slug_book)
    return render(request, 'book_app/one_book.html', {
        "book": book
    })