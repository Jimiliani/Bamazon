from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('books/', ),
    path('book/<int:pk>', ),
    path('author/<int:pk>', ),
    path('author/<int:pk>/books', ),
]
