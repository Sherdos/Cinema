from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from film.models import Movie
from film.serializers import MovieSerializer


class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CategoryAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        movies = Movie.objects.filter(category__slug=slug)
        return movies
