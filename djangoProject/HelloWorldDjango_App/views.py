from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HelloPage(request):
    return HttpResponse('<ht style="color:red"> Hello World!</h1>')
