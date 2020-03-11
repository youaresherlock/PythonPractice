from django.urls import path
from .views import Music, Movie, Book

urlpatterns = [
    path('music', Music.as_view()),
    path('movie', Movie.as_view()),
    path('book', Book.as_view())
]