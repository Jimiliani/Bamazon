from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views import View

from api.serializers import BooksListSerializer
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
        book = get_object_or_404(Book, pk=pk)
        print(book)
        return render(request, self.template_name)


class AuthorDetail(View):
    template_name = 'books/author_detail.html'
    paginated_by = 2

    def get(self, request, pk, *args, **kwargs):
        author = get_object_or_404(Author, pk=pk)
        books = Book.objects.filter(authors__in=[author]).order_by('name')
        paginator = Paginator(books, self.paginated_by)
        page_number = request.GET.get('page')
        page_of_book = paginator.get_page(page_number)
        for i in page_of_book:
            print(i)
        print(page_of_book)
        return render(request, self.template_name)
