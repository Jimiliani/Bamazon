from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import BooksListSerializer, BookDetailSerializer, AuthorDetailSerializer, AuthorsListSerializer
from books.models import Book, Author


class BooksList(ListAPIView):
    """ Список книг """
    serializer_class = BooksListSerializer

    def get_queryset(self):
        books = Book.objects.prefetch_related('authors')
        return books


class BookDetail(RetrieveAPIView):
    """ Информация об отдельной книге """
    serializer_class = BookDetailSerializer

    def get_queryset(self):
        books = Book.objects.prefetch_related('authors', 'authors__books')
        return books


class AuthorsList(ListAPIView):
    """ Список авторов """
    serializer_class = AuthorsListSerializer

    def get_queryset(self):
        authors = Author.objects.prefetch_related('books')
        return authors


class AuthorDetail(RetrieveAPIView):
    """ Информация об отдельном авторе """
    serializer_class = AuthorDetailSerializer

    def get_queryset(self):
        authors = Author.objects.prefetch_related('books', 'books__authors')
        return authors
