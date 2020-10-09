from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField(null=False, blank=False)
    authors = models.ManyToManyField('Author', on_delete=models.PROTECT, null=False, blank=False, related_name='books')


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    about = models.TextField()
