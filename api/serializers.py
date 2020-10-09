from rest_framework import serializers

from books.models import Book, Author


class AuthorNameSerializer(serializers.ModelSerializer):
    """

    Вывод полного имени автора

    """

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']


class BookNameSerializer(serializers.ModelSerializer):
    """

    Вывод названия книги

    """

    class Meta:
        model = Book
        fields = ['id', 'name']


class AuthorsListSerializer(serializers.ModelSerializer):
    """

    Вывод списка авторов

    """
    books = BookNameSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class BooksListSerializer(serializers.ModelSerializer):
    """

    Вывод списка книг

    """
    authors = AuthorNameSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorDetailSerializer(serializers.ModelSerializer):
    """

    Вывод полной информации об авторе

    """
    books = BooksListSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    """

    Вывод полной информации о книге

    """
    authors = AuthorsListSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
