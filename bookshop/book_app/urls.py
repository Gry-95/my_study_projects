from django.urls import path
from book_app import views

urlpatterns = [
    path('', views.show_all_books),
    path('book/<str:slug_book>', views.show_one_book, name='book-detail'),
    path('authors/', views.show_authors),
    path('authors/<int:id_author>', views.show_author, name='author-detail')
]
