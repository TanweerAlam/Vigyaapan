from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about', views.AboutView.as_view(), name="about"),
    path('contact', views.contactView, name="contact"),
    path('privacy-policy', views.PrivacyPolicyView.as_view(), name="privacy-policy"),
    path('disclaimer', views.DisclaimerView.as_view(), name="disclaimer"),
    path('tnc', views.TermNConditionView.as_view(), name="tnc"),
]