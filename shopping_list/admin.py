from django.contrib import admin
from .models import ShoppingItem
from .models import Category


admin.site.register(ShoppingItem)
admin.site.register(Category)
