from django import forms
from .models import ShoppingItem
from .models import Category


class ShopItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['item', 'brand', 'quantity']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-field'}),
            'brand': forms.TextInput(attrs={'class': 'form-field'}),
            'quantity': forms.TextInput(attrs={'class': 'form-field'}),
        }




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        widgets = {'category': forms.TextInput(attrs={'class': 'form-field'})}