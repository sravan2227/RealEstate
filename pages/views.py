from django.shortcuts import render
from django.http import HttpResponse

# we can functions here and display it thru urls.py


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
