from django import forms
from .models import ShoppingItem, Category


class ShopItemForm(forms.ModelForm):

    """ Form to add and edit items """

    class Meta:
        model = ShoppingItem
        fields = ['item', 'brand', 'quantity']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-field'}),
            'brand': forms.TextInput(attrs={'class': 'form-field'}),
            'quantity': forms.TextInput(attrs={'class': 'form-field'}),
        }


class CategoryForm(forms.ModelForm):

    """ Form to add categories"""

    class Meta:
        model = Category
        fields = ['category']
        widgets = {'category': forms.TextInput(attrs={'class': 'form-field'})}
