from django import forms
from .models import ShoppingItem
from .models import AddCategory


class ShopItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['name', 'brand', 'quantity']

    # def __init__(self, *args, **kwargs):
    #     categories = kwargs.pop('categories')
    #     super(ShopItemForm, self).__init__(*args, **kwargs)
    #     self.fields['category'].queryset = categories


class CategoryForm(forms.ModelForm):
    class Meta:
        model = AddCategory
        fields = ['category']
