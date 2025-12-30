from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
    path("add/<int:pk>/", ReviewCreateView.as_view(), name="review-add"),
]
