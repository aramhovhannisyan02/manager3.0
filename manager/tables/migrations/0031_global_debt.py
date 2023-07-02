# Generated by Django 4.2 on 2023-06-30 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0030_alter_paymant_options_remove_debt_seen_delete_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Global_Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt', models.IntegerField()),
                ('timeOfCreating', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]