from django.urls import include, path
from rest_framework import routers

from film.views.views_movie import MovieViewSet
from film.views.views_order import GenreOrderAPIView, SearchAPIView

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')


urlpatterns = [
    path('', include(router.urls)),
    path('genre/<slug:slug>/', GenreOrderAPIView.as_view(), name='order_genre'),
    path('search/', SearchAPIView.as_view()),
]
