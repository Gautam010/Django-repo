from django.shortcuts import render
from .models import *
from django.http import *
def index(request):
    d=Post.objects.all()
    for i in d:
        print(i.title)
        print (i.text)
    return HttpResponse('hello')
# Create your views here.
