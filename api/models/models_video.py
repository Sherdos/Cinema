from datetime import date

from django.db import models

from api.models.models_other import Category, Genre


class BaseVideo(models.Model):
    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание', null=True, blank=True)
    poster = models.URLField('ссылка на постер')
    video = models.URLField('ссылка на видео')
    year = models.PositiveSmallIntegerField('Дата выхода', default=date.today())
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)

    class Meta:
        abstract = True


class Movie(BaseVideo):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Serial(BaseVideo):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сериял'
        verbose_name_plural = 'Сериалы'


class Season(models.Model):

    description = models.TextField('Описание')
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE, verbose_name='Сериал')

    def __str__(self):
        return f'{self.serial}'

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class Seria(models.Model):

    title = models.CharField('название', max_length=50)
    description = models.TextField('Описание')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name='Сезон')

    def __str__(self):
        return f'{self.season}'

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'


class MovieShots(models.Model):
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie.id}'

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'
