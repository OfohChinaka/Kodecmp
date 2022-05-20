from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return HttpResponse('<p> About me </p>')

def contact(request):
    return HttpResponse('<b> Contact me </b>')
