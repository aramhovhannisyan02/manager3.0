# Generated by Django 4.2 on 2023-07-01 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0034_bigtablerows_delete_weektables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bigtablerows',
            name='bigTable',
        ),
        migrations.RemoveField(
            model_name='bigtablerows',
            name='table',
        ),
    ]
