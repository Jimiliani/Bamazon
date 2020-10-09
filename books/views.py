from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views import View

from api.serializers import BooksListSerializer, AuthorDetailSerializer, BookDetailSerializer
from books.models import Book, Author


class BooksList(View):
    template_name = 'books/books_list.html'
    paginated_by = 2

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        books = BooksListSerializer(books, many=True).data
        paginator = Paginator(books, self.paginated_by)
        page_number = request.GET.get('page')
        page_of_book = paginator.get_page(page_number)
        return render(request, self.template_name, {'page': page_of_book})


class BookDetail(View):
    template_name = 'books/books_detail.html'

    def get(self, request, pk, *args, **kwargs):
        book = Book.objects.prefetch_related('authors').get(pk=pk)
        book = BookDetailSerializer(book).data
        print(book)
        return render(request, self.template_name, {'book': book})


class AuthorDetail(View):
    template_name = 'books/author_detail.html'
    paginated_by = 2

    def get(self, request, pk, *args, **kwargs):
        author = Author.objects.prefetch_related('books').get(pk=pk)
        author = AuthorDetailSerializer(author).data
        return render(request, self.template_name, {'author': author})
