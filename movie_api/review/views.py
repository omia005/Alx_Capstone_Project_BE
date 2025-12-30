from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Review
from .forms import ReviewForm
from movies.models import Movie

#create your views here
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "review/review_form.html"

    def form_valid(self, form):
        movie = Movie.objects.get(pk=self.kwargs["pk"])
        form.instance.movie = movie
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("movie-detail", kwargs={"pk": self.kwargs["pk"]})