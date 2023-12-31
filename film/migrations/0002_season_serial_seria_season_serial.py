# Generated by Django 4.2.4 on 2023-08-28 09:53

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сезон',
                'verbose_name_plural': 'Сезоны',
            },
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('poster', models.URLField(verbose_name='ссылка на постер')),
                ('year', models.PositiveSmallIntegerField(default=datetime.date(2023, 8, 28), verbose_name='Дата выхода')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                 to='film.category', verbose_name='Категория')),
                ('genres', models.ManyToManyField(to='film.genre', verbose_name='жанры')),
            ],
            options={
                'verbose_name': 'Сериял',
                'verbose_name_plural': 'Сериалы',
            },
        ),
        migrations.CreateModel(
            name='Seria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('video', models.URLField(verbose_name='ссылка на видео')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.season', verbose_name='Сезон')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
        migrations.AddField(
            model_name='season',
            name='serial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='film.serial', verbose_name='Сериал'),
        ),
    ]
