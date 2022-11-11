from django.shortcuts import render, redirect
from django.views import generic, View
from django.http import HttpResponse
from .models import ShoppingItem
from .forms import ItemForm


def home(request):
    return render(request,'index.html')


def get_shoppinglist(request):
    items = ShoppingItem.objects.all()
    context = {
        'items': items
    }
    return render(request,'shopping_list.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://8000-stealthy20-groceryshopp-2w8l8dbjpwl.ws-eu75.gitpod.io/shopping_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'add_item.html', context)
