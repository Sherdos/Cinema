
from rest_framework.generics import ListAPIView
from api.models.models_movie import Movie

from api.serializers import MovieSerializer


class GenreOrderAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        movies = Movie.objects.filter(genres__url=slug)
        return movies
    
class SearchAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        name = self.request.GET.get('key')
        print(name)
        movies = Movie.objects.filter(title__icontains=name)
        return movies
    