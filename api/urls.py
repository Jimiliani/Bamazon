from django.urls import path

from api.views import BooksList, BookDetail, AuthorDetail, AuthorsList

urlpatterns = [
    path('books/', BooksList.as_view(), name='api-books-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='api-book-detail'),
    path('authors/', AuthorsList.as_view(), name='api-authors-list'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='api-author-detail'),
]
