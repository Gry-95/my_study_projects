# Generated by Django 4.2.3 on 2023-08-17 14:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
