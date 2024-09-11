from django.shortcuts import render
from .models import Author, Book, Publisher

# Create your views here.
def get_info(request):
    book = Book.objects.get(id=1)
    return render(request, 'base.html', context={
        'book': book,
    })
    
def get_author(request):
    book_author = Book.objects.filter(author__name="А. С. Пушкин")
    return render(request, 'author.html', context={
        'book_author': book_author,
    })
    
def  get_all_author(request):
    author = Author.objects.exclude(name="А. С. Пушкин")
    return render(request, 'allAuthor.html', context={
      'author': author,  
    })

def get_publisher(request):
    publisher = Publisher.objects.all()
    return render(request, "publisher.html", context={
        'publisher': publisher,
    })