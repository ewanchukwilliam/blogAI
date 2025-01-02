from django.http import HttpResponse
from django.shortcuts import resolve_url
from django.template.loader import render_to_string


class HtmxRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.htmx and response.status_code in [301, 302]:
            # Get the redirect URL
            redirect_url = response.url
            
            # If redirecting to homepage, render the home partial
            if redirect_url == "/" or redirect_url == "/home":
                content = render_to_string(
                    "core/partials/home_partial.html",
                    {"user_authenticated": request.user.is_authenticated},
                    request=request
                )
                return HttpResponse(content)
            
            # For other redirects, set HX-Redirect header
            response['HX-Redirect'] = redirect_url
            
        return response
