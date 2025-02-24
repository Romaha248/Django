from django.urls import path

from . import views

urlpatterns = [
    path("<int:month>", views.monthly_chall_by_num),
    path("<str:month>", views.monthly_chall, name="month_chall"),
    path("", views.monthes)

]