from django.urls import path

from books.views import BooksList, BookDetail, AuthorDetail

urlpatterns = [
    path('books/', BooksList.as_view(), name='books-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]
