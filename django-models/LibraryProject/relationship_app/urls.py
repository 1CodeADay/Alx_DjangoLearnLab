from django.urls import path, include
from django.contrib import admin
from .views import list_books
from .views import home, LibraryDetailView


urlpatterns = [

    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("", home, name="home"),  # Ajoute la page d'accueil ici
]
