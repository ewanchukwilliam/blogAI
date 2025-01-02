from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from authentication.forms import CustomUserCreationForm
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


def login_view(request):
    # Initialize form with styled widgets
    form = AuthenticationForm()
    form.fields['username'].widget.attrs.update({
        'class': 'input input-bordered w-full',
        'placeholder': 'Enter your username'
    })
    form.fields['password'].widget.attrs.update({
        'class': 'input input-bordered w-full',
        'placeholder': 'Enter your password'
    })
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    
    template = "authentication/partials/login_partial.html" if request.htmx else "authentication/login.html"
    return render(request, template, {"form": form})


@login_required  # This ensures only logged-in users can logout
def logout_view(request):
    logout(request)
    if request.htmx:
        # If it's an HTMX request, return the login form
        from django.contrib.auth.forms import AuthenticationForm
        form = AuthenticationForm()
        return render(request, "authentication/partials/login_partial.html", {"form": form})
    return redirect('login')  # Redirect to login page for regular requests


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    
    template = "authentication/partials/register_partial.html" if request.htmx else "authentication/register.html"
    return render(request, template, {"form": form})


@login_required
def profile_view(request):
    template = "core/partials/profile_partial.html" if request.htmx else "core/profile.html"
    return render(request, template, {})


def logout_view(request):
    logout(request)
    return redirect('login')


# Create your views here.
