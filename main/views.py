from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Main


# Create your views here.

class IndexView(TemplateView):
    template_name = "main/index.html"
    extra_context = {'site' : Main.objects.get(page__icontains="home")}
    
    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     context['site'] = Main.objects.get(page__icontains="home")
    #     return context
    

class AboutView(TemplateView):
    template_name = "main/about.html"
    extra_context = {'site' : Main.objects.get(page__icontains="about")}
    
class ContactView(TemplateView):
    template_name = "main/contact.html"
    extra_context = {'site' : Main.objects.get(page__icontains="contact")}