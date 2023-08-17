from rest_framework import serializers

from api.models.models_other import RatingStar

class RatingStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingStar
        fields='__all__'






