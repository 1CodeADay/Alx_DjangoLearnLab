from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book

from django.views.generic.detail import DetailView
from .models import Library

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
