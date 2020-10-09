from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View

from books.models import Book, Author


class BooksList(View):
    template_name = 'books/books_list.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        print(books)
        return render(request, self.template_name)


class BookDetail(View):
    template_name = 'books/books_detail.html'

    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        print(book)
        return render(request, self.template_name)


class AuthorDetail(View):
    template_name = 'books/author_detail.html'

    def get(self, request, pk, *args, **kwargs):
        author = get_object_or_404(Author, pk=pk)
        print(author)
        return render(request, self.template_name)


class AuthorBooks(View):
    template_name = 'books/author_books.html'
    paginated_by = 2

    def get(self, request, pk, *args, **kwargs):
        author = get_object_or_404(Author, pk=pk)
        books = Book.objects.filter(authors__in=[author]).order_by('name')
        paginator = Paginator(books, self.paginated_by)
        page_number = request.GET.get('page')
        page_of_books = paginator.get_page(page_number)
        print(page_of_books)
        print(books)
        print(paginator)
        for i in page_of_books:
            print(i)
        return render(request, self.template_name)
