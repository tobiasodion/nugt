from django.shortcuts import render
from django.http import HttpResponse

from .utils.indexer import indexFile

def index(request):
    result = indexFile("file.txt")
    context = {'message': result}
    return render(request, 'mysite/index.html', context)

