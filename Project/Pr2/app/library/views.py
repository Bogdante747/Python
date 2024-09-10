from django.shortcuts import render

# Create your views here.
def get_library(request):
    return render(request, 'library.html', {
        'title': 'Книга',
        'book': 'Евгений Онегин А. С. Пушкин',
    })