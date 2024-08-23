from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_page(request):
    return HttpResponse('This is the blog page')