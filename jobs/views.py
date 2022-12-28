from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.db.models import Q

from .models import Job, State
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
        query = self.request.GET.get('search', None)
        if query:
            return Job.objects.filter(
                Q(post_title__icontains=query) | Q(post_title__icontains=query)
            )
        

class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = "jobs/job_list.html"

class JobDetailView(DetailView):
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


class SuperUserPassesTestMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        return HttpResponse('<h1>Sorry, you are not authorised to access this page. Please, ask the admin...</h1>')

class StateListView(SuperUserPassesTestMixin, ListView):
    model = State
    template_name = 'jobs/state_list.html'

class StateCreateView(SuperUserPassesTestMixin, CreateView):
    model = State
    template_name = 'jobs/add_update_state.html'

class StateUpdateView(SuperUserPassesTestMixin, UpdateView):
    model = State
    template_name = 'jobs/add_update_state.html'

class StateDeleteView(SuperUserPassesTestMixin, DeleteView):
    model = State
    template_name = 'jobs/delete_state.html'
