from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


# Each view = a page
class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
