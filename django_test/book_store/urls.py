from django.urls import path
from . import views
from .views import create_book, get_books, update_book, delete_book


urlpatterns = [
    path("", views.index, name="index"),
    path('create/', create_book, name='create_book'),
    path('books/', get_books, name='get_books'),
    path('books/<int:book_id>/', views.view_book, name='view_book'),  # Added this line
    path('update/<int:book_id>/', update_book, name='update_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
]
