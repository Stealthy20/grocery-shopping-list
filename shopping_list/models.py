from django.db import models
from django.contrib.auth.models import User


class AddCategory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ["category"]


class ShoppingItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    name = models.CharField(max_length=50, blank=False)
    brand = models.CharField(max_length=50, blank=True)
    quantity = models.CharField(max_length=50, blank=True, default=1)
    category = models.ForeignKey(AddCategory, on_delete=models.CASCADE, null=True)
    taken = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["category"]
