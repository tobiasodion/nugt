from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    result = "Hello, world. You're at the polls index."
    return HttpResponse(result)
