from django import forms
from .models import ShoppingItem
from .models import Category


class ShopItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['item', 'brand', 'quantity']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
