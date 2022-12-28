from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path('jobs', views.Home.as_view(), name="home"),
    path('jobs/list', views.JobListView.as_view(), name="jobList"),

    path('jobs/search/', views.SearchListView.as_view(), name="search_results"),

    path('jobs/create', views.JobCreateView.as_view(), name="createJob"),
    path('jobs/<slug:slug>', views.JobDetailView.as_view(), name="jobDetail"),
    path('jobs/<slug:slug>/update', views.JobUpdateView.as_view(), name="updateJob"),
    path('jobs/<slug:slug>/delete', views.JobDeleteView.as_view(), name="deleteJob"),
]