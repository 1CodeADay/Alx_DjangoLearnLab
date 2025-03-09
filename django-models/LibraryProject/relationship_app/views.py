from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.

def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil !")


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Create this template
    context_object_name = "library"
