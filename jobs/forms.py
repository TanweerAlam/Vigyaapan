from django.forms import ModelForm, widgets
from django import forms
from datetime import date
import datetime
from .models import Job, State

from django.utils.translation import gettext_lazy as _
from tinymce.widgets import TinyMCE


# QUALIFICATION = [
#     ('MATRIC', _('Matriculation')),
#     ('INTERMEDIATE', _('Intermediate')),
#     ('GRADUATION', _('Graduate/Bachelors')),
#     ('POST-GRADUATION', _('Post-graduate/Masters')),
#     ('DOCTORATE', _('Ph.D/Doctorate'))
# ]

# APPLICATION = [
#     ('ONLINE', _('Online')),
#     ('OFFLINE', _('Offline'))
# ]

# STATE = State.objects.all()

# class JobForm(forms.Form):
#     post_title = forms.CharField(max_length=200, initial='Default name')
#     brief_intro = forms.CharField(widget=forms.Textarea, max_length=500, initial='Brief introduction of the job post')

#     body = forms.CharField(widget=forms.Textarea, max_length=500, initial='Information of the job post')

#     notification_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': date.today()}))
#     online_application_date = forms.DateField(widget= forms.DateInput(attrs={'type': 'date', 'min': date.today().year - 1}))
#     application_expiry_date = forms.DateField(widget= forms.DateInput(attrs={'type': 'date', 'min': date.today().year}))
#     application_mode = forms.CharField(max_length=30,  widget=forms.Select(choices=APPLICATION))
#     application_link = forms.URLField(empty_value='')

#     minimum_age = forms.IntegerField(min_value=17, max_value=30)
#     maximum_age = forms.IntegerField(min_value=18, max_value=60)

#     minimum_qualification = forms.CharField(max_length=30,  widget=forms.Select(choices=QUALIFICATION))

#     dept_of_ministry = forms.CharField(max_length=50, required=False)
#     total_posts = forms.IntegerField(min_value=0)

#     # state = forms.ChoiceField(choices=STATE)
#     application_fee = forms.IntegerField(min_value=0)
#     official_site = forms.URLField(empty_value='')

#     admit_card_link = forms.URLField(empty_value='')
#     notification_link = forms.URLField(empty_value='')

# class JobCreationForm(JobForm, ModelForm):
#     class Meta:
#         fields = JobForm
#         model = Job


# class JobCreationForm(ModelForm):
#     # required_css_class = 'form-control'
#     class Meta:
#         model = Job
#         # fields = ['post_title', 'brief_intro', 'notification_date', 'online_application_date', 'application_mode', 'application_link', 'application_expiry_date',
#         # 'minimum_age', 'maximum_age', 'minimum_qualification', 'dept_of_ministry', 'total_posts', 'state', 'application_fee', 'official_site',
#         # 'admit_card_link', 'notification_link']
#         fields = ('__all__')
#         post_title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'place-holder': 'Title'})),
#         widgets = {
#             'notification_date': widgets.DateInput(attrs={'type': 'date', 'max': date.today()}),
#             'online_application_date': widgets.DateInput(attrs={'type': 'date', 'min': date.today().year - 1}),
#             'application_expiry_date': widgets.DateInput(attrs={'type': 'date', 'min': date.today()}),
#         }



class JobCreationUpdationForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('slug', 'author')
        fields = ('__all__')
        post_title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'place-holder': 'Title'})),
        content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
        widgets = {
            'notification_date': widgets.DateInput(attrs={'type': 'date', 'max': date.today()}),
            'online_application_date': widgets.DateInput(attrs={'type': 'date', 'min': date.today().year - 1}),
            'application_expiry_date': widgets.DateInput(attrs={'type': 'date', 'min': date.today()}),
        }