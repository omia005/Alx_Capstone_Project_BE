from django.urls import path
from .views import MovieListView, MovieDetailView, RegisterView

urlpatterns = [
    path("", MovieListView.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("register/", RegisterView.as_view(), name="register"),
]
