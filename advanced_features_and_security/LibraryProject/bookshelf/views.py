from django.shortcuts import render

# Step 3: Enforce Permissions in Views

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

@permission_required('bookshelf.can_view', raise_exception=True)
""" def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books}) """

def book_list(request):
    search_term = request.GET.get('search', '')  # Get the search term from the GET request
    books = Book.objects.filter(title__icontains=search_term)  # Filter books based on search term
    return render(request, 'bookshelf/book_list.html', {'books': books, 'search_term': search_term})


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            # Proceed with creating the book
            Book.objects.create(**form.cleaned_data)

# bookshelf/views.py

from .forms import ExampleForm

def book_search(request):
    books = Book.objects.all()
    form = ExampleForm(request.GET)

    if form.is_valid():
        search_term = form.cleaned_data['search_term']
        books = Book.objects.filter(title__icontains=search_term)

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
