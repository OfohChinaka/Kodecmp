from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    return render(request, 'accounts/register.html')

def login(request):
    return HttpResponse('<b> login here </b>')

def checkout(request):
    return HttpResponse('<p> Jhalyn Checkout </p>')