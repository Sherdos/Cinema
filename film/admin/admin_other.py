from django.contrib import admin
from django.utils.safestring import mark_safe

from film.models.models_base import Category, Genre
from film.models.models_movie import MovieShots


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)
    prepopulated_fields = {'url': ['name']}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('name', 'url')
    prepopulated_fields = {'url': ['name']}


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ('movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    # get_image.short_description = 'Изображение'
