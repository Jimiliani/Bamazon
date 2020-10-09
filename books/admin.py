from django.contrib import admin
from django.contrib.auth.models import User, Group

from books.models import Book, Author

admin.site.site_header = 'Книги и авторы'


class BookAdmin(admin.ModelAdmin):
    """

    Кастомизация панели книг в админке

    """
    list_display = ['name', 'price', 'length']
    list_filter = ['name', 'price', 'length']
    filter_horizontal = ['authors', ]


class AuthorAdmin(admin.ModelAdmin):
    """

    Кастомизация панели авторов в админке

    """
    list_display = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
