# Generated by Django 4.2.3 on 2023-08-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dressingroom',
            name='floor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dressingroom',
            name='number',
            field=models.IntegerField(),
        ),
    ]
