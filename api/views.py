from rest_framework.generics import *
from .models import *
from .serializers import *


class MovieAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CategoryAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        movies = Movie.objects.filter(category__slug=slug)
        return movies

class GenreAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        movies = Movie.objects.filter(genre__slug=slug)
        return movies
    
class SearchAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        name = self.request.GET.get('key')
        print(name)
        movies = Movie.objects.filter(title=name)
        return movies