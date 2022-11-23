from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponse
from django.contrib import messages
import django_filters
from .models import ShoppingItem
from .models import AddCategory
from .forms import ShopItemForm
from .forms import CategoryForm



def home(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def get_shoppinglist(request):
    items = ShoppingItem.objects.all()
    return render(request, 'shopping_list.html', {'items': items})


@login_required(login_url='/accounts/login/')
def get_categories(request):
    categories = AddCategory.objects.all()
    return render(request, 'get_categories.html', {'categories': categories})


@login_required(login_url='/accounts/login/')
def add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item = form.save()
            messages.success(request, 'You successfully added the category')
            return redirect('addcat')
    form = CategoryForm()
    return render(request, 'add_categories.html', {'form': form})


@login_required(login_url='/accounts/login/')
def add_item(request):
    if request.method == 'POST':
        form = ShopItemForm(request.POST)
        category_id = request.POST.get("categories")
        if category_id:
            category = get_object_or_404(AddCategory, id=category_id)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.category = category
                item = form.save()
                messages.success(request, 'You successfully added the item')
                return redirect(reverse('add_item'))
        else:
            messages.error(request, 'You need to add a Category before adding a item to the Shopping List')
            return redirect('add')
    categories = AddCategory.objects.filter(user=request.user)
    form = ShopItemForm()
    return render(request, 'add_item.html', {'form': form, 'categories': categories})


@login_required(login_url='/accounts/login/')
def edit_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    if request.method == 'POST':
        form = ShopItemForm(request.POST, instance=item)
        category_id = request.POST.get("categories")
        category = get_object_or_404(AddCategory, id=category_id)
        if form.is_valid():
            item = form.save(commit=False)
            item.category = category
            item = form.save()
            messages.success(request, 'You successfully updated the item')
            return redirect('shopping_list')
    categories = AddCategory.objects.filter(user=request.user)
    form = ShopItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'categories': categories})



@login_required
def delete_item(request, item_id):
    item = get_object_or_404(ShoppingItem, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect('shopping_list')


def toggle_item(request, item_id):
    item = get_object_or_404(ShoppingItem, id=item_id)
    item.taken = not item.taken
    item.save()
    return redirect('shopping_list')



@login_required
def delete_cat(request, category_id):
    category = get_object_or_404(AddCategory, pk=category_id)
    category.delete()
    messages.success(request, 'Category deleted successfully')
    return redirect('shopping_list')
