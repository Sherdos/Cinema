
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from api.models.models_movie import Genre, Movie

from api.serializers.serializers_movie import MovieSerializer


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
    