from django.contrib import admin
from django.utils.safestring import mark_safe

from film.models.models_movie import MovieShots


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    # get_image.short_description = 'Изображение'
