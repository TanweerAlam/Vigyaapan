# users/urls.py

from django.urls import path, include
from users.views import DashboardView, SignUpView

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "users"

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("signup/", SignUpView.as_view(), name="signup")
]