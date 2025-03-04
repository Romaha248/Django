from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import (
    Review,
)  #!!!!Model and Form separate approach or to update existing models

# Create your views here.

# class approach
# class ReviewView(View): # with View
#     def get(self, request):
#         form = ReviewForm()

#         return render(
#             request,
#             "reviews/reviews.html",
#             {
#                 "form": form,
#             },
#         )
#     def post(self, request):
#         # existing_review = Review.objects.get(pk=1)  # to update existing models
#         form = ReviewForm(request.POST)  # also add instance here to update

#         # if form.is_valid():
#         # review = Review(
#         #     username=form.cleaned_data["username"],
#         #     review=form.cleaned_data["review"],
#         #     rating=form.cleaned_data["rating"],
#         # )
#         # review.save()
#         # return redirect("/thanks-you") !!!!Model and Form separate approach

#         if form.is_valid():
#             form.save()
#             return redirect("/thanks-you")  # ModelForm approach

#         return render(
#             request,
#             "reviews/reviews.html",
#             {
#                 "form": form,
#             },
#         )

# class ReviewView(FormView): # with FormView
#     form_class = ReviewForm
#     template_name = "reviews/reviews.html" # this handling get request
#     success_url = "/thanks-you"

#     def form_valid(self, form): # this handling post request
#         form.save()
#         return super().form_valid(form)


class ReviewView(CreateView):  # with CreateView
    model = Review
    form_class = ReviewForm  # to handel more options like name a labels and set error messages
    # fields = "__all__"
    template_name = "reviews/reviews.html"  # this handling get request
    success_url = "/thanks-you"

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return redirect("/thanks-you")

    #     return render(
    #         request,
    #         "reviews/reviews.html",
    #         {
    #             "form": form,
    #         },
    #     )


# func approach
# def reviews(request):
#     if request.method == "POST":
#         # existing_review = Review.objects.get(pk=1)  # to update existing models
#         form = ReviewForm(request.POST)  # also add instance here to update

# if form.is_valid():
# review = Review(
#     username=form.cleaned_data["username"],
#     review=form.cleaned_data["review"],
#     rating=form.cleaned_data["rating"],
# )
# review.save()
# return redirect("/thanks-you") !!!!Model and Form separate approach

#     if form.is_valid():
#         form.save()
#         return redirect("/thanks-you")  # ModelForm approach
# else:
#     form = ReviewForm()

# return render(
#     request,
#     "reviews/reviews.html",
#     {
#         "form": form,
#     },
# )


class ThanksView(TemplateView):
    template_name = "reviews/thanks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=1)
        return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_reviews = Review.objects.get(pk=review_id)
    #     context["review"] = selected_reviews
    #     return context # Template View


# def thanks(request):
#     return render(request, "reviews/thanks.html")
