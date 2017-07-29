from django.shortcuts import render, redirect
from ..reg_login.models import User
from .models import Author, Book, Review

# Create your views here.
def index(req):
    context = {
        'user': User.objects.get(id=req.session['user_id']),
        'recent': Review.objects.all().order_by('-created_at')[:3],
        'books': Book.objects.all()
    }
    return render(req, 'books/index.html', context)

def add_book_review(req):
    context = {
        'authors': Author.objects.all()
    }
    return render(req, 'books/add.html', context)

def process(req, route):
    if route=='new':
        id = Book.objects.add(req)
        Review.objects.add(req, id)
        return redirect('books:book_page', id=id)
    elif route=='remote':
        Review.objects.add_remote(req)
        return redirect('books:book_page', id=req.session['book_id'])

def book_page(req, id):
    req.session['book_id'] = id
    current_book = Book.objects.get(id=id)
    context = {
        'book': current_book,
        'book_reviews': current_book.reviews.all().order_by('-created_at')
    }
    return render(req, 'books/book.html', context)

def delete(req, id):
    book_id = Review.objects.get(id=id).book_id.id
    Review.objects.filter(id=id).delete()
    return redirect('books:book_page', id=book_id)

def logout(req):
    req.session.flush()
    return redirect('reg_login:index')
