from ast import List

# from django.http import (HttpResponse, HttpResponseBadRequest,
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

# from django.urls import reverse


def homepage(request):
    user_authenticated = request.user.is_authenticated
    return render(request, "core/Homepage.html", {"user_authenticated": user_authenticated})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


# # Create your views here.
# def homepageview(request):
#     return HttpResponse("this is the blogai homepage!")
#
#
# argumentkeys = {"stinky": "You are stinky", "smelly": "You are smelly"}
#
#
# def dynamicURL(request, arguments):
#     try:
#         output = argumentkeys[arguments]
#     except:
#         return HttpResponseNotFound("This page was not found")
#     redirect_path = reverse("dynamicURL", args=[arguments])
#     return HttpResponse(output)
#
#
# def dynamicNumber(response, arguments):
#     return HttpResponse(f"this is the number in the url {arguments}")
#
#
# month_names = {
#     "january": "this is january",
#     "february": "this is february",
#     "march": "this is march",
#     "april": "this is april",
#     "may": "this is may",
#     "june": "this is june",
#     "july": "this is july",
#     "august": "this is august",
#     "september": "this is september",
#     "october": "this is october",
#     "november": "this is november",
#     "december": "this is december",
# }
#
#
# def month_number(request, month):
#     if month >= 12 or month < 0:
#         return HttpResponseBadRequest("This is not a valid month")
#     months = list(month_names.keys())
#     month = months[month - 1]
#     path_redirect = reverse("month", args=[month])
#     return HttpResponseRedirect(path_redirect)
#
#
# def month(request, month):
#     return HttpResponse(month_names[month])
#
