from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view: List all books
def list_all_books(request):
    books = Book.objects.all()  # must be exactly this
    return render(request, 'relationship_app/list_books.html', {'books': books})  # must be exactly this

# Class-based view: Library detail including its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
