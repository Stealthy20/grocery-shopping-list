from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from .models import ShoppingItem


def home(request):
    return render(request,'index.html')


def get_shoppinglist(request):
    items = ShoppingItem.objects.all()
    context = {
        'items': items
    }
    return render(request,'shopping_list.html', context)
