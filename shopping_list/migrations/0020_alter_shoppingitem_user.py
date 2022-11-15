# Generated by Django 3.2.16 on 2022-11-15 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping_list', '0019_alter_shoppingitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
