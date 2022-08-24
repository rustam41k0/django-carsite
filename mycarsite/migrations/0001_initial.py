# Generated by Django 4.0.5 on 2022-06-23 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255, verbose_name='Текст комментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=255, verbose_name='Главный заголовок')),
                ('main_text', models.TextField(max_length=255, verbose_name='Главное описание')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=255, verbose_name='Описание')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(to='mycarsite.comments')),
                ('tags', models.ManyToManyField(to='mycarsite.tags')),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('category', models.ManyToManyField(to='mycarsite.category')),
            ],
        ),
    ]
