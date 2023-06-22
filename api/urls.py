from django.urls import path
from .views import *

urlpatterns = [
    path('list/', MovieAPIView.as_view()),
    path('list/<slug:slug>/', CategoryAPIView.as_view()),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view()),
    path('search/', SearchAPIView.as_view()),

]