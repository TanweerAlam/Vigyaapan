from django.urls import path
from . import views

app_name = 'newsletters'

urlpatterns = [
    path('new/', views.new, name="new"),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
]