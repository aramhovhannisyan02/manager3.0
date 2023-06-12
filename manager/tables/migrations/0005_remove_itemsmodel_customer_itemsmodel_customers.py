# Generated by Django 4.2 on 2023-05-17 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0004_itemsmodel_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsmodel',
            name='customer',
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='customers',
            field=models.ManyToManyField(related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]