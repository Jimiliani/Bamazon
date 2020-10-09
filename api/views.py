from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import BooksListSerializer, BookDetailSerializer, AuthorDetailSerializer, AuthorsListSerializer
from books.models import Book, Author


class BooksList(ListAPIView):
    """ Список книг """
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer


class BookDetail(RetrieveAPIView):
    """ Информация об отдельной книге """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class AuthorsList(ListAPIView):
    """ Список авторов """
    queryset = Author.objects.all()
    serializer_class = AuthorsListSerializer


class AuthorDetail(RetrieveAPIView):
    """ Информация об отдельном авторе """
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
