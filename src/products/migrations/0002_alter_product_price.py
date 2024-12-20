# Generated by Django 5.1.4 on 2024-12-10 20:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='in US dollars $', max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
