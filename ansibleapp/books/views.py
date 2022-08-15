from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Book

class BookListView(LoginRequiredMixin , ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book_list.html'