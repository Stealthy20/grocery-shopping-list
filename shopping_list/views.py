from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponse
from django.contrib import messages
from .models import ShoppingItem
from .forms import ItemForm


def home(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def get_shoppinglist(request):
    items = ShoppingItem.objects.all()
    context = {
        'items': items
    }
    return render(request,'shopping_list.html', context)

@login_required(login_url='/accounts/login/')
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully added the item')
            return redirect('add')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'add_item.html', context)

@login_required(login_url='/accounts/login/')
def edit_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully updated the item')
            return redirect('shopping_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'edit_item.html', context)


def delete_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.delete()
    messages.success(request, 'You successfully deleted the item')
    return redirect('shopping_list')


def toggle_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.taken = not item.taken
    item.save()
    return redirect('shopping_list')
