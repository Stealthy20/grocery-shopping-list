from django import forms
from .models import ShoppingItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['name', 'brand', 'quantity', 'category', 'user']