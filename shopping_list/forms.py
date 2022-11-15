from django import forms
from .models import ShoppingItem
from .models import AddCategory


class ShopItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['name', 'brand', 'quantity', 'category',]


class CategoryForm(forms.ModelForm):
    model = AddCategory
    fields = ['category']
