from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    """
    Category Model
    -----------
    Model for Users Item
    Attributes:
    -----------
    user:
        Link to User model
    Category:
        Name of the category used for ShoppingItem
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ["category"]


class ShoppingItem(models.Model):

    """
    ShoppingItem Model
    -----------
    Model for Users Item
    Attributes:
    -----------
    user:
        Link to User model
    item:
        Name of the item in the shopping list
    brand:
        optional field to clarify the brand of the item
    quantity:
        Charfield to put in the amount of that product you need, ex 1kg.
    category:
        Link to the Category Model
    picked:
        Boolean field to check if item is picked or not
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    item = models.CharField(max_length=50, blank=False)
    brand = models.CharField(max_length=50, blank=True)
    quantity = models.CharField(max_length=50, blank=True, default='ex 1 kg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                        blank=True, null=True)
    picked = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["category"]
