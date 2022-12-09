from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponse
from django.contrib import messages
import django_filters
from .models import ShoppingItem, Category
from .forms import ShopItemForm, CategoryForm


def home(request):

    """ A View for rendering home page"""

    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def shopping_list(request):

    """ A View for rendering items to shopping list """

    items = ShoppingItem.objects.all()
    return render(request, 'shopping_list.html', {'items': items})


@login_required(login_url='/accounts/login/')
def add_item(request):

    """ A View to render the form for the user to add new items """

    if request.method == 'POST':
        form = ShopItemForm(request.POST)
        category_id = request.POST.get("categories")
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.category = category
                item = form.save()
                messages.success(request, 'You successfully added the item')
                return redirect('add_item')
        else:
            messages.error(request, 'You need to add a Category before\
                adding a item to the Shopping List')
            return redirect('add_item')
    categories = Category.objects.filter(user=request.user)
    form = ShopItemForm()
    return render(
        request, 'add_item.html', {'form': form, 'categories': categories})


@login_required(login_url='/accounts/login/')
def edit_item(request, item_id):

    """ A View to render the form for the user to edit items """

    item = get_object_or_404(ShoppingItem, id=item_id)
    if request.method == 'POST':
        form = ShopItemForm(request.POST, instance=item)
        category_id = request.POST.get("categories")
        category = get_object_or_404(Category, id=category_id)
        if form.is_valid():
            item = form.save(commit=False)
            item.category = category
            item = form.save()
            messages.success(request, 'You successfully updated the item')
            return redirect('shopping_list')
    categories = Category.objects.filter(user=request.user)
    form = ShopItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'categories': categories})


def delete_item(request, item_id):

    """ A View for the user to delete items"""

    item = get_object_or_404(ShoppingItem, id=item_id)
    item.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect('shopping_list')


def toggle_item(request, item_id):

    """ A View for the user to toggle items """

    item = get_object_or_404(ShoppingItem, id=item_id)
    item.picked = not item.picked
    item.save()
    return redirect('shopping_list')


@login_required(login_url='/accounts/login/')
def category(request):

    """ A View to render the form for the user to ad new categories  """

    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item = form.save()
            messages.success(request, 'You successfully added the category')
            return redirect('category')
    form = CategoryForm()
    return render(request, 'category.html', {'form': form, 'categories': categories})


def delete_category(request, category_id):

    """ A View for the user to delete categories """

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category deleted successfully')
    return redirect('category')


def delete_list(request):

    """ A View for the user to delete all items in the list"""

    items = ShoppingItem.objects.all()
    items.user = request.user
    for item in items:
        if item.user == request.user:
            item.delete()
    return redirect('shopping_list')
