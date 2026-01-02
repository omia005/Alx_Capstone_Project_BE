from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from movies.models import Movie

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
    template_name = "reviews/review_form.html"

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse("movie-detail", kwargs={"pk": self.object.movie.pk})


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse("movie-detail", kwargs={"pk": self.object.movie.pk})