# bookshelf/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('book_search/', views.book_search, name='book_search'),
    path('book_list/', views.list_books, name='book_list'),
]


