# Generated by Django 5.0.2 on 2024-02-15 10:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemist_backend', '0003_sales_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
