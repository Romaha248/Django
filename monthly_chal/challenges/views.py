from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": None,
}

# Create your views here.


def monthly_chall_by_num(request, month):
    months = list(challanges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    forward_month = months[month - 1]
    redirect_path = reverse(
        "month_chall", args=[forward_month]
    )  # challenge/(month we choose)
    return HttpResponseRedirect(redirect_path)


def monthly_chall(request, month):
    try:
        text_chal = challanges[month]
        return render(
            request,
            "challenges/challenge.html",
            {
                "text": text_chal,
                "month": month,
            },
        )
    except:
        raise Http404()


def monthes(request):
    months = list(challanges.keys())

    return render(request, "challenges/index.html", {"months": months})
