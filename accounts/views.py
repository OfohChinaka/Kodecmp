from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    return HttpResponse('<p> Signup here </p>')

def login(request):
    return HttpResponse('<b> login here </b>')

def checkout(request):
    return HttpResponse('<p> Jhalyn Checkout </p>')