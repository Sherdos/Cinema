from django.db import models

from film.models.models_movie import BaseVideo


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
    video = models.URLField('ссылка на видео')

    def __str__(self):
        return f'{self.season}'

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'
