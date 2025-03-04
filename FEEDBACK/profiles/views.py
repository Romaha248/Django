from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile
# Create your views here.

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    template_name = "profiles/user_profile.html"
    model = UserProfile
    context_object_name = "images"

    

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form,
#         })

#     def post(self, request):
#         sub_form = ProfileForm(request.POST, request.FILES)

#         if sub_form.is_valid():
#             # store_file(request.FILES["image"])
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return redirect("/profiles")
        
#         return render(request, "profiles/create_profile.html", {
#             "form": sub_form,
#         })