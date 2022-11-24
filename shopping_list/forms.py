from django import forms
from .models import ShoppingItem
from .models import Category


class ShopItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['name', 'brand', 'quantity']




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
