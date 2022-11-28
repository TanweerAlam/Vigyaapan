from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class State(models.Model):
    state_code = models.CharField(max_length=10, null=False, blank=False)
    state = models.CharField(max_length=30, null=True, blank=False)

    def __str__(self):
        return self.state


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
    state = models.ForeignKey(State, related_name='jobs', on_delete=models.SET_DEFAULT, default='Central')

    brief_intro = models.TextField(max_length=500, default='Brief introduction of the job post')
    body = models.TextField(max_length=500, default='Information of the job post', null=True, blank=True)
    
    notification_date = models.DateField(null=True, blank=True)
    online_application_date = models.DateField(null=True, blank=True)
    application_expiry_date = models.DateTimeField(null=True, blank=True)
    # post_updated_date = models.DateField()

    application_mode = models.CharField(max_length=30, choices=APPLICATION)
    application_link = models.URLField(null=True, blank=True)

    minimum_age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(17), MaxValueValidator(30)])
    maximum_age = models.PositiveIntegerField(default=28, validators=[MinValueValidator(18), MaxValueValidator(60)])
    minimum_qualification = models.CharField(max_length=50, choices=QUALIFICATION)

    dept_of_ministry = models.CharField(max_length=50, null=True, blank=True)
    total_posts = models.PositiveIntegerField()
    application_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    official_site = models.URLField(null=True, blank=True)
    admit_card_link = models.URLField(null=True, blank=True)
    notification_link = models.URLField(null=True, blank=True)

    isPublished = models.BooleanField(default=False, verbose_name="Published?")

    created_on = models.DateField(auto_now_add=True, editable=False)
    updated_on = models.DateField(auto_now=True)

    slug = models.SlugField(max_length=300, blank=True, null=True)

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
        return reverse('jobDetail', kwargs={'slug': self.slug})
