from django.contrib import admin
from api.admin.inline_admin import MovieShotsInline, ReviewInline

from api.models.models_movie import Category, Genre, Movie, MovieShots
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)
    prepopulated_fields = {'url' : ['name']}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "category", "url",)
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    prepopulated_fields = {'url' : ['title']}
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
        }),
        (None, {
            "fields": (("year"),)
        }),
        (None, {
            "fields": (("genres", "category"),)
        }),
        ("Options", {
            "fields": (("url",  ),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Постер"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")
    prepopulated_fields = {'url' : ['name']}
    


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"



