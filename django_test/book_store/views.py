from django.shortcuts import render

from django.http import HttpResponse
from book_store.models import Book


def index(request):
    return HttpResponse("Welcome to my book store.")

def create_book(request):
    book = Book.objects.create(
        title="The Alchemist",
        author="Paulo Coelho",
        price=19.99,
        genre="Fiction"
    )
    return HttpResponse({"message": "Book created!", "book_id": book.id})

def get_books(request):
    books = Book.objects.all().values()
    return HttpResponse(list(books), safe=False)

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.price = 15.99  # Example: updating the price
    book.save()
    return HttpResponse({"message": "Book updated!"})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return HttpResponse({"message": "Book deleted!"})

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_store/view_book.html', {'book': book})
