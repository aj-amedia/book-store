from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse, Http404
from django.db.models import Avg, Min


# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    agg_rating = books.aggregate(Avg('rating'), Min('rating')) # rating__avg, rating__min


    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_number_of_books': num_books,
        'agg_rating': agg_rating
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_best_seller": book.is_best_selling,
    })