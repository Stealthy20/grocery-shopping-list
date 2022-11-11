from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Not taken"), (1, "Taken"))


class AddCategory(models.Model):

    category = models.CharField(max_length=50, unique=True, blank=False)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ["category"]


class ShoppingItem(models.Model):

    name = models.CharField(max_length=50, blank=False)
    brand = models.CharField(max_length=50, blank=True)
    quantity = models.FloatField(default=1)
    category = models.ForeignKey(AddCategory, on_delete=models.CASCADE, null=True)
    item_taken = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["category"]
