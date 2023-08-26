from django.db import models
from datetime import date
from api.models.models_movie import Category, Genre



class BaseFilm(models.Model):
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание",  null=True, blank=True)
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=date.today())
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    
    class Meta:
        abstract = True