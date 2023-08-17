from rest_framework.generics import CreateAPIView
from api.models.models_other import Rating, RatingStar, Reviews

from api.serializers import RatingStarSerializer, ReviewSerializer


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