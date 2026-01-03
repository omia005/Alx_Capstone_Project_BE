from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Movie
from django.urls import reverse_lazy

# Create your views here.


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("login")


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "movies"
    paginate_by = 6
    

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
    context_object_name = "movie"