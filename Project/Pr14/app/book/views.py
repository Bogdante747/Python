from django.shortcuts import render

# Create your views here.
def get_home(requset):
    return render(requset, 'home.html')