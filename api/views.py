from rest_framework.generics import *
from rest_framework.viewsets import *
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CategoryAPIView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        movies = Movie.objects.filter(category__slug=slug)
        return movies

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
    
    
class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Reviews

class RatingCreateAPIView(CreateAPIView):
    serializer_class = RatingStarSerializer
    queryset = RatingStar

    def create(self, request, *args, **kwargs):
        movie = request.data['movie']
        del request.data['images']
        rating = super().create(request, *args, **kwargs)
        Rating.objects.create(star=rating, movie_id=movie)
        return rating
