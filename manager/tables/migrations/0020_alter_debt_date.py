# Generated by Django 4.2 on 2023-06-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0019_debt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
