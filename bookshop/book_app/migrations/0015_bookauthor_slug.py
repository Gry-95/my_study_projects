# Generated by Django 4.2.3 on 2023-08-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0014_remove_bookauthor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookauthor',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]