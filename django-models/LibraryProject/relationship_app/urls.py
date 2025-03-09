from django.urls import path, include
from django.contrib import admin
from .views import list_books
from .views import home, LibraryDetailView

from django.contrib.auth import views as auth_views
from . import views

from .views import admin_view, librarian_view, member_view



urlpatterns = [

    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("", home, name="home"),  # Ajoute la page d'accueil ici

    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Use built-in LoginView
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Use built-in LogoutView
    path('register/', views.register, name='register'),  # Custom register view

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

     path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]

