from __future__ import unicode_literals
from django.db import models
from ..reg_login.models import User

# Create your models here.
class BookManager(models.Manager):
    def add(self, request):
        data = request.POST
        #Check for Book
        if len(self.filter(title=data['title'])) < 1:
            current_book = self.create(
                title = data['title']
            )
            # Add Author
            if len(data['author_name']) < 1:
                add_author = Author.objects.get(name=data['author'])
            else:
                add_author = Author.objects.create(name=data['author_name'])

            current_book.author.add(add_author)
        else:
            current_book = self.get(title=data['title'])
        return current_book.id

class ReviewManager(models.Manager):
    def add(self, request, book_id):
        data = request.POST
        #Check for Book
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=request.session['user_id'])
        self.create(content=data['review'], rating=int(data['rating']), user_id=user, book_id=book)

    def add_remote(self, request):
        data = request.POST
        book = Book.objects.get(id=request.session['book_id'])
        user = User.objects.get(id=request.session['user_id'])
        self.create(content=data['review'], rating=int(data['rating']), user_id=user, book_id=book)


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __str__(self):
        return self.title

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user_id = models.ForeignKey(User, related_name="reviews")
    book_id = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
