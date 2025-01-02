from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def login_view(request):
    # Initialize form variable
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    
    # Choose template based on HTMX request
    template = "authentication/partials/login_partial.html" if request.htmx else "authentication/login_form.html"
    return render(request, template, {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.htmx:
                return render( request, "authentication/partials/login_partial.html",
                    {"form": AuthenticationForm()},
                )
            return redirect("login")
    else:
        form = UserCreationForm()
    template = "authentication/partials/register_partial.html" if request.htmx else "authentication/register_form.html"
    return render(request, template, {"form": form})


# Create your views here.
