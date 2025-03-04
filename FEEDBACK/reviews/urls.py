from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="form"),
    path("thanks-you", views.ThanksView.as_view()),
    path("all-reviews", views.ReviewsListView.as_view(), name="all_reviews"),
    path("all-reviews/<int:pk>", views.SingleReviewView.as_view(), name="review"),
]
