from ast import List

from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseNotFound, HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def homepageview(request):
    return HttpResponse("this is the blogai homepage!")


argumentkeys = {"stinky": "You are stinky", "smelly": "You are smelly"}


def dynamicURL(request, arguments):
    try:
        output = argumentkeys[arguments]
    except:
        return HttpResponseNotFound("This page was not found")
    redirect_path = reverse("dynamicURL", args=[arguments])
    return HttpResponse(output)


def dynamicNumber(response, arguments):
    return HttpResponse(f"this is the number in the url {arguments}")


month_names = {
    "january": "this is january",
    "february": "this is february",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "july": "this is july",
    "august": "this is august",
    "september": "this is september",
    "october": "this is october",
    "november": "this is november",
    "december": "this is december",
}


def month_number(request, month):
    if month >= 12 or month < 0:
        return HttpResponseBadRequest("This is not a valid month")
    months = list(month_names.keys())
    month = months[month - 1]
    path_redirect = reverse("month", args=[month])
    return HttpResponseRedirect(path_redirect)


def month(request, month):
    return HttpResponse(month_names[month])


def homepage(request):
    return render(request, "Homepage.html")
