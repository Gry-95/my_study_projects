# Generated by Django 4.2.3 on 2023-08-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]