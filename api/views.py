from rest_framework.generics import *
from .models import *
from .serializers import *


class MovieAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
