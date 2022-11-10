from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse


def home(request):
    return render(request,'index.html')
