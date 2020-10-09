from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from api.serializers import BooksListSerializer, AuthorDetailSerializer, BookDetailSerializer
from books.models import Book, Author


class BooksList(View):
    """

    Список книг

    """
    template_name = 'books/books_list.html'
    paginated_by = 2

    def get(self, request, *args, **kwargs):
        books = Book.objects.prefetch_related('authors').order_by('name').all()
        books = BooksListSerializer(books, many=True).data
        paginator = Paginator(books, self.paginated_by)
        page_number = request.GET.get('page')
        page_of_book = paginator.get_page(page_number)
        return render(request, self.template_name, {'page': page_of_book})


class BookDetail(View):
    """

    Информация об отдельной книге

    """
    template_name = 'books/books_detail.html'

    def get(self, request, pk, *args, **kwargs):
        book = Book.objects.prefetch_related('authors', 'authors__books').get(pk=pk)
        book = BookDetailSerializer(book).data
        return render(request, self.template_name, {'book': book})


class AuthorDetail(View):
    """

    Информация об отдельном авторе

    """
    template_name = 'books/author_detail.html'
    paginated_by = 2

    def get(self, request, pk, *args, **kwargs):
        author = Author.objects.prefetch_related('books', 'books__authors').get(pk=pk)
        author = AuthorDetailSerializer(author).data
        return render(request, self.template_name, {'author': author})
