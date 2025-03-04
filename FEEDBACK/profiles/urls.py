from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("all_images", views.ProfilesView.as_view()),
]
