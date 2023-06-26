from rest_framework import serializers
from .models import *



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields='__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields='__all__'

class RatingStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingStar
        fields='__all__'






