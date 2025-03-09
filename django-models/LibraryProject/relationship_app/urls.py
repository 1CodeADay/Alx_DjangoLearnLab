from django.urls import path, include
from django.contrib import admin
from .views import list_books
from .views import home, LibraryDetailView

from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [

    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("", home, name="home"),  # Ajoute la page d'accueil ici

    path('login/', auth_views.LoginView.as_view(), name='login'),  # Use built-in LoginView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Use built-in LogoutView
    path('register/', views.register, name='register'),  # Custom register view
]
