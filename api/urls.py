from django.urls import path
from .views import *

urlpatterns = [
    path('list/', MovieAPIView.as_view())
]