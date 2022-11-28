from django.forms import ModelForm, widgets
from django import forms
from datetime import date
from .models import Job
class JobCreationForm(ModelForm):
    # required_css_class = 'form-control'
    class Meta:
        model = Job
        fields = ['post_title', 'brief_intro', 'notification_date', 'online_application_date', 'application_mode', 'application_link', 'application_expiry_date',
        'minimum_age', 'maximum_age', 'minimum_qualification', 'dept_of_ministry', 'total_posts', 'state', 'application_fee', 'official_site',
        'admit_card_link', 'notification_link']
        post_title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'place-holder': 'Title'})),
        widgets = {
            'notification_date': widgets.DateInput(attrs={'type': 'date', 'max': date.today()}),
            'online_application_date': widgets.DateInput(attrs={'type': 'date', 'min': date.today().year - 1}),
            'application_expiry_date': widgets.DateInput(attrs={'type': 'date', 'min': date.today()}),
        }