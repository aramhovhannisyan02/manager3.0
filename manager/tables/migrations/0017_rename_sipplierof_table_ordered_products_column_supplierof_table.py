# Generated by Django 4.2 on 2023-06-08 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0016_ordered_products_column_sipplierof_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordered_products_column',
            old_name='sipplierof_table',
            new_name='supplierof_table',
        ),
    ]
