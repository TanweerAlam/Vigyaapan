from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path('jobs/tags', views.TagListView.as_view(), name="tagList"),
    path('jobs/tags/<slug:slug>', views.JobListByTagView.as_view(), name="job_list_by_tags"),
    path('jobs/list', views.JobListView.as_view(), name="jobList"),
    path('jobs/list_by_<str:keyword>', views.jobLists, name="list_by_type"),
    path('jobs/search', views.SearchListView.as_view(), name="search_results"),
    path('jobs/<slug:slug>', views.JobDetailView.as_view(), name="jobDetail"),

    # path('jobs/create', views.JobCreateView.as_view(), name="createJob"),
    # path('jobs/<slug:slug>/update', views.JobUpdateView.as_view(), name="updateJob"),
    # path('jobs/<slug:slug>/delete', views.JobDeleteView.as_view(), name="deleteJob"),

    
]