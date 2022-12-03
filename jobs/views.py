from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)

from .models import Job
from .forms import JobCreationUpdationForm

# Create your views here.

class Home(TemplateView):
    template_name = "jobs/home.html"
    
class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = "jobs/job_list.html"

class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = "jobs/job_detail.html"
    # pk_url_kwarg = 'pk'

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobCreationUpdationForm
    template_name = "jobs/add_update_job.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobCreationUpdationForm
    template_name = "jobs/add_update_job.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'jobs/delete_job.html'
    success_url = reverse_lazy('jobs:jobList')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user