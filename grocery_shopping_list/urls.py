"""grocery_shopping_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shopping_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('shopping_list', views.shopping_list, name="shopping_list"),
    path('add_item', views.add_item, name='add_item'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('delete_item/<str:item_id>/', views.delete_item, name="delete_item"),
    path('toggle/<item_id>', views.toggle_item, name='toggle'),
    path('category', views.category, name="category"),
    path(
        'delete_category/<category_id>',
        views.delete_category, name='delete_category'),
    path('delete_list', views.delete_list, name='delete_list'),
    path('accounts/', include('allauth.urls')),
]
