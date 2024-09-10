from django.shortcuts import HttpResponse

# Create your views here.
def get_hello(request):
    return HttpResponse('<h1>Hello world!</h1>')