# Generated by Django 3.2.16 on 2022-11-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0006_alter_shopingitem_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopingitem',
            name='brand',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]