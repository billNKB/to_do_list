from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request, name):
    return HttpResponse('bonjour a tous ' + name)
