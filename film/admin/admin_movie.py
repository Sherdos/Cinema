from django.contrib import admin
from django.utils.safestring import mark_safe

from film.admin.inline import MovieShotsInline
from film.admin.shema import movie
from film.models.models_movie import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    """Фильмы"""
    list_display = ['title', 'category', 'url', 'get_image']
    list_filter = ['category', 'year']
    search_fields = ['title', 'category__name']
    prepopulated_fields = {'url': ['title']}
    inlines = [MovieShotsInline]
    save_on_top = True
    save_as = True
    readonly_fields = ['get_image']
    fieldsets = movie

    def get_image(self, obj: Movie):
        return mark_safe(f'<img src={obj.poster} width="20%"')

    # get_image.short_description = 'Постер'
