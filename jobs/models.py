from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from django.conf import settings
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

from taggit.managers import TaggableManager


# Create your models here.
class State(models.Model):
    # state_code = models.CharField(max_length=10, unique=True, null=False, blank=False)
    state = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.state


    # def get_default_state():
    #     return State.objects.all().first()



class Job(models.Model):
    # Education choices
    QUALIFICATION = [
        ('MATRIC', _('Matriculation')),
        ('INTERMEDIATE', _('Intermediate')),
        ('GRADUATION', _('Graduate/Bachelors')),
        ('POST-GRADUATION', _('Post-graduate/Masters')),
        ('DOCTORATE', _('Ph.D/Doctorate'))
    ]
    APPLICATION = [
        ('ONLINE', _('Online')),
        ('OFFLINE', _('Offline'))
    ]

    post_title = models.CharField(max_length=200, default='Default name', null=False, blank=False)
    # state = models.CharField(max_length=30, default='Central')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    tags = TaggableManager()

    brief_intro = models.TextField(max_length=500, default='Brief introduction of the job post')
    # body = models.TextField(max_length=500, default='Information of the job post', null=True, blank=True)
    content = HTMLField()
    # exam_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
    
    notification_date = models.DateField(null=True, blank=True)
    online_application_date = models.DateField(null=True, blank=True)
    application_expiry_date = models.DateTimeField(null=True, blank=True)
    # post_updated_date = models.DateField()

    application_mode = models.CharField(max_length=30, choices=APPLICATION)
    application_link = models.URLField(null=True, blank=True, default='')

    minimum_age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(17), MaxValueValidator(30)])
    maximum_age = models.PositiveIntegerField(default=28, validators=[MinValueValidator(18), MaxValueValidator(60)])
    minimum_qualification = models.CharField(max_length=50, choices=QUALIFICATION)

    dept_of_ministry = models.CharField(max_length=50, null=True, blank=True)
    total_posts = models.PositiveIntegerField()
    application_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    # .....
    fee_last_date = models.DateField(null=True, blank=True)
    correction_date = models.DateField(null=True, blank=True)
    exam_date = models.DateField(null=True, blank=True)
    # .....

    # .....
    general_obc_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
    sc_st_ph_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
    female_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
    # .....

    official_site = models.URLField(null=True, blank=True, default='')
    admit_card_link = models.URLField(null=True, blank=True, default='')
    notification_link = models.URLField(null=True, blank=True, default='')
    result_link = models.URLField(null=True, blank=True, default='')
    syllabus_link = models.URLField(null=True, blank=True, default='')
    answerkey_link = models.URLField(null=True, blank=True, default='')

    is_featured = models.BooleanField(default=False, verbose_name="Featured job?")
    is_admission = models.BooleanField(default=False, verbose_name="Is admission?")
    is_published = models.BooleanField(default=False, verbose_name="Published?")

    created_on = models.DateField(auto_now_add=True, editable=False)
    updated_on = models.DateField(auto_now=True)

    slug = models.SlugField(max_length=300, blank=True, null=True, default='')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

        ordering=['-application_expiry_date']


    def __str__(self):
        return self.post_title


    def save(self, *args, **kwargs):
        if not self.slug and self.post_title:
            self.slug = slugify(self.post_title + "  " + str(self.state) + " " + str(self.total_posts))
        return super(Job, self).save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('jobs:jobDetail', kwargs={"slug": self.slug})


# class Admission(models.Model):
    
#     admission_name = models.CharField(max_length=200, default='Default name', null=False, blank=False)
#     admission_started_on = models.DateField(null=True, blank=True)
#     brief_intro = models.TextField(max_length=500, default='Brief introduction of the admission to the course')
#     # important_dates =
#     application_fees = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
#     course_name = models.CharField(max_length=200, default='Default name', null=False, blank=False)
#     eligibility = models.CharField(max_length=50, choices=QUALIFICATION)
#     instructions = HTMLField()
#     admission_link = models.URLField(null=True, blank=True, default='')

#     def __str__(self):
#         return self.admission_name