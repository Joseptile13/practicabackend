from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    http = """
    <h1>APP 2</h1>
    <h2>Vista 1</h2>
    <h3>joseacuna</h3>
    """
    return HttpResponse(http)

def vista2(request):
    http = """
    <h1>APP 2</h1>
    <h2>Vista 2</h2>
    <h3>joseacuna_2</h3>
    """
    return HttpResponse(http)
