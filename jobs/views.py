from django.http import HttpResponse
from django.shortcuts import render
# from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
#  CreateView, DeleteView 
# from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Job, State
from .forms import JobCreationUpdationForm

from datetime import date

# Create your views here.

def jobLists(request, keyword):
    print(keyword)
    job_list = None
    page_number = request.GET.get('page')

    today = date.today()

    if keyword == 'admit-card':
        job_list = Job.objects.filter(admit_card_link__isnull=False, is_published=True).order_by('-updated_on').values('post_title', 'slug')
    elif keyword == 'result':
        job_list = Job.objects.filter( result_link__isnull=False, is_published=True).order_by('-updated_on').values('post_title', 'slug')
    elif keyword == 'syllabus':
        job_list = Job.objects.filter(syllabus_link__isnull=False, is_published=True).order_by('-updated_on').values('post_title', 'slug')
    elif keyword == 'answerkey':
        job_list = Job.objects.filter(answerkey_link__isnull=False, is_published=True).order_by('-updated_on').values('post_title', 'slug')
    elif keyword == 'admission':
        job_list = Job.objects.filter(is_admission=True, is_published=True).order_by('-updated_on').values('post_title', 'slug')

    paginator = Paginator(job_list, 2) # Show 50 jobs per page.
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobs/list_by_type.html', {'keyword': keyword, 'page_obj': page_obj, 'paginator': paginator})


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
        

# class JobListView(LoginRequiredMixin, ListView):
class JobListView(ListView):
    model = Job
    template_name = "jobs/job_list.html"
    paginate_by = 50

class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/job_detail.html"
    # pk_url_kwarg = 'pk'

# class JobCreateView(LoginRequiredMixin, CreateView):
#     model = Job
#     form_class = JobCreationUpdationForm
#     template_name = "jobs/add_update_job.html"

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Job
#     form_class = JobCreationUpdationForm
#     template_name = "jobs/add_update_job.html"

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user

# class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Job
#     template_name = 'jobs/delete_job.html'
#     success_url = reverse_lazy('jobs:jobList')

#     def test_func(self):
#         obj = self.get_object()
#         return obj.author == self.request.user


# class SuperUserPassesTestMixin(LoginRequiredMixin, UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.is_superuser
    
#     def handle_no_permission(self):
#         return HttpResponse('<h1>Sorry, you are not authorised to access this page. Please, ask the admin...</h1>')

# class StateListView(SuperUserPassesTestMixin, ListView):
#     model = State
#     template_name = 'jobs/state_list.html'

# class StateCreateView(SuperUserPassesTestMixin, CreateView):
#     model = State
#     template_name = 'jobs/add_update_state.html'

# class StateUpdateView(SuperUserPassesTestMixin, UpdateView):
#     model = State
#     template_name = 'jobs/add_update_state.html'

# class StateDeleteView(SuperUserPassesTestMixin, DeleteView):
#     model = State
#     template_name = 'jobs/delete_state.html'
