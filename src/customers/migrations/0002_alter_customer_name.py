# Generated by Django 5.1.4 on 2024-12-10 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(help_text="Customer's business name", max_length=120),
        ),
    ]
