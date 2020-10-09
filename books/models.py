from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(null=False, blank=False, verbose_name='Цена')
    image = models.ImageField(default='cover/default.jpg', upload_to='cover/', null=False,
                              verbose_name='Изображение обложки')
    length = models.IntegerField(null=False, blank=False, verbose_name='Длина')
    authors = models.ManyToManyField('Author', blank=False, related_name='books', verbose_name='Авторы')

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Фамилия')
    image = models.ImageField(default=' authors/default.jpg', upload_to='authors/', null=False,
                              verbose_name='Изображение автора')
    about = models.TextField(verbose_name='Об авторе')

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
