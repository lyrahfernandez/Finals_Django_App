# myapp/views.py
from django.views.generic import ListView, DetailView
from .models import Book, Author, Publisher, Reader

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publishers'

class ReaderListView(ListView):
    model = Reader
    template_name = 'reader_list.html'
    context_object_name = 'readers'
