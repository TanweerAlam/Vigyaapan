from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import Job
from .forms import JobCreationForm



# Create your views here.

class Home(TemplateView):
    template_name = "jobs/home.html"
    
class JobListView(ListView):
    model = Job
    template_name = "jobs/job_list.html"

class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/job_detail.html"
    # pk_url_kwarg = 'pk'

class JobCreateView(CreateView):
    model = Job
    # fields = ("__all__")
    form_class = JobCreationForm
    template_name = "jobs/add_update_job.html"

class JobUpdateView(UpdateView):
    model = Job
    fields = ("__all__")
    exclude = ('slug')
    template_name = "jobs/add_update_job.html"

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/delete_job.html'
    success_url = reverse_lazy('jobs:jobList')