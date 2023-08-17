from django.urls import path,include

from api.views.views_movie import MovieViewSet
from api.views.views_order import GenreOrderAPIView, SearchAPIView
from api.views.views_other import RatingCreateAPIView, ReviewCreateAPIView
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')


urlpatterns = [
    path('', include(router.urls)),
    path('genre/<slug:slug>/', GenreOrderAPIView.as_view()),
    path('search/', SearchAPIView.as_view()),
    path('create/review/', ReviewCreateAPIView.as_view()),
    path('create/rating/', RatingCreateAPIView.as_view()),

]