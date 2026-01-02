from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Review
from .forms import ReviewForm
from movies.models import Movie
from django.db.models import Q

#create your views here
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ["content", "rating"]
    template_name = "review/review_form.html"

    def form_valid(self, form):
        movie = Movie.objects.get(pk=self.kwargs["pk"])
        form.instance.movie = movie
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("movie-detail", kwargs={"pk": self.kwargs["pk"]})
    
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "review/review_form.html"

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse("movie-detail", kwargs={"pk": self.object.movie.pk})


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "review/confirm_delete.html"

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse("movie-detail", kwargs={"pk": self.object.movie.pk})
    
class ReviewSearchView(ListView):
    model = Review
    template_name = "review/review_search.html"
    context_object_name = "reviews"

    def get_queryset(self):
        queryset = Review.objects.select_related("movie", "user")

        query = self.request.GET.get("q")
        rating = self.request.GET.get("rating")

        if query:
            queryset = queryset.filter(
                Q(movie__title__icontains=query)
            )

        if rating:
            queryset = queryset.filter(rating=rating)

        return queryset