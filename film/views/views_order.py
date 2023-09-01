from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from film.models import Genre, Movie
from film.serializers import MovieSerializer


class GenreOrderAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        get_object_or_404(Genre, url=slug)
        movies = Movie.objects.filter(genres__url=slug).prefetch_related('genres')
        return movies


class SearchAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        name = self.request.GET.get('key')
        movies = Movie.objects.filter(title__icontains=name)
        return movies
