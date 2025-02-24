from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


challanges = {
    "january": "eat",
    "february": "sleep",
    "march": "code",
    "april": "repeat",
    "may": "eat",
    "june": "sleep",
    "july": "code",
    "august": "repeat",
    "september": "eat",
    "october": "sleep",
    "november": "code",
    "december": "repeat",

}

# Create your views here.

def monthly_chall_by_num(request, month):
    months = list(challanges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    forward_month = months[month - 1]
    redirect_path = reverse("month_chall", args=[forward_month]) # challenge/(month we choose)
    return HttpResponseRedirect(redirect_path)

def monthly_chall(request, month):
    try:
        text = challanges[month]
        response_text = f"<h1>{text}</h1>"
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound("<h1>This monnth not supp</h1>")
    
def monthes(request):
    list_items = ""
    months = list(challanges.keys())

    for month in months:
        month_path = reverse("month_chall", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"

    data = f"<ul>{list_items}</ul>"
    return HttpResponse(data)
    
