# Generated by Django 4.0.5 on 2022-06-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarsite', '0005_alter_posts_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='comments',
            field=models.ManyToManyField(blank=True, to='mycarsite.comments'),
        ),
    ]
