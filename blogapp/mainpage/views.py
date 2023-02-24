from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.

def mainpage(request):
    return render(request, 'mainpage/index.html')
