# Generated by Django 4.0.5 on 2022-06-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarsite', '0008_alter_posts_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время написания'),
        ),
    ]
