# Generated by Django 3.2.16 on 2022-11-14 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0010_auto_20221114_1821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='shoppingitem',
            name='user',
        ),
    ]
