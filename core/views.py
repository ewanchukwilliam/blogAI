from django.shortcuts import redirect, render
from django.contrib.auth import logout

def homepage(request):
    user_authenticated = request.user.is_authenticated
    template = "core/partials/home_partial.html" if request.htmx else "core/homepage.html"
    return render(request, template, {"user_authenticated": user_authenticated})

def logout_view(request):
    logout(request)
    return redirect("home")

def refresh_sidebar(request):
    return render(request, 'components/sidebar.html')
