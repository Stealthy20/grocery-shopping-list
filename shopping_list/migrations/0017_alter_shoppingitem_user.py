# Generated by Django 3.2.16 on 2022-11-15 11:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping_list', '0016_alter_shoppingitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
