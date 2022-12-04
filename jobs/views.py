from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.db.models import Q

from .models import Job
from .forms import JobCreationUpdationForm

# Create your views here.

class Home(TemplateView):
    template_name = "jobs/home.html"

class SearchListView(ListView):
    model = Job
    context_object_name = 'job_list'
    template_name = 'jobs/search_results.html'

    # queryset = Job.objects.filter(post_title__icontains="engineers")
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Job.objects.filter(
            Q(post_title__icontains=query) | Q(post_title__icontains=query)
        )

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

class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    form_class = JobCreationUpdationForm
    template_name = "jobs/add_update_job.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = 'jobs/delete_job.html'
    success_url = reverse_lazy('jobs:jobList')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user