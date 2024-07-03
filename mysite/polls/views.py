from django.shortcuts import render
from django.http import HttpResponse

from .utils.indexer import indexFile

def index(request):
    result = indexFile("file.txt")
    return HttpResponse(result)
