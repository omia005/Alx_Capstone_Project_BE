from django.urls import path
from .views import ReviewCreateView, ReviewDeleteView, ReviewUpdateView, ReviewSearchView

urlpatterns = [
    path("add/<int:pk>/", ReviewCreateView.as_view(), name="review-add"),
    path("<int:pk>/edit/", ReviewUpdateView.as_view(), name="review-edit"),
    path("<int:pk>/delete/", ReviewDeleteView.as_view(), name="review-delete"),
    path("search/", ReviewSearchView.as_view(), name="review-search"),
]
