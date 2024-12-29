from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    Entry Point for the application

    :param TemplateView: Description of `TemplateView`
    :TemplateView TemplateView: Type of `TemplateView`
    :example:  = HomeView(TemplateView)
    """
    template_name = "home.html"
    def get_context_data(self, **k):
        context = super().get_context_data(**k)
        if self.request.htmx:
            self.template_name = "partials/home_content.html"
        return context


# Create your views here.
