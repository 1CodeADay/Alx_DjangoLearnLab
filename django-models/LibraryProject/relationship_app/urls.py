from django.urls import path, include
from .views import home, list_books, LibraryDetailView
from django.contrib import admin


urlpatterns = [

    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("", home, name="home"),  # Ajoute la page d'accueil ici
]
