# Generated by Django 3.2.16 on 2022-11-12 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0008_rename_shopingitem_shoppingitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingitem',
            name='item_taken',
        ),
        migrations.AddField(
            model_name='shoppingitem',
            name='taken',
            field=models.BooleanField(default=False),
        ),
    ]
