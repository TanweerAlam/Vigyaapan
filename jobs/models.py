from django.db import models
from django.utils.text import slugify
# from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# from django.conf import settings
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

# from taggit.managers import TaggableManager
from taggit_autosuggest.managers import TaggableManager

# for image uploading
from django.core.files import File
from io import BytesIO
from PIL import Image


# Create your models here.
class State(models.Model):
    # state_code = models.CharField(max_length=10, unique=True, null=False, blank=False)
    # state = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super(State, self).save(*args, **kwargs)
    # def get_default_state():
    #     return State.objects.all().first()

class Ministry(models.Model):
    name = models.CharField(max_length=180, null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Ministry'
        verbose_name_plural = 'Ministries'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super(Ministry, self).save(*args, **kwargs)


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

    keywords = models.CharField(max_length=200, default='Default name', null=False, blank=False)

    post_title = models.CharField(max_length=200, default='Default name', null=False, blank=False)
    image = models.ImageField(upload_to='jobs_image/%Y/%m/', blank=True, null=True)
    state = models.ForeignKey(State, related_name="jobs", on_delete=models.SET_NULL, default=None, null=True, blank=True)
    # dept_of_ministry = models.CharField(max_length=50, null=True, blank=True)
    ministry = models.ForeignKey(Ministry, related_name="jobs", on_delete=models.SET_NULL, default=None, null=True, blank=True)
    tags = TaggableManager()

    brief_intro = models.TextField(max_length=600, default='Brief introduction of the job post')
    content = HTMLField()

    notification_date = models.DateField(null=True, blank=True)
    online_application_date = models.DateField(null=True, blank=True)
    application_expiry_date = models.DateTimeField(null=True, blank=True)
    # post_updated_date = models.DateField()

    application_mode = models.CharField(max_length=30, choices=APPLICATION)
    application_link = models.URLField(null=True, blank=True, default='')

    # minimum_age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(17), MaxValueValidator(30)])
    # maximum_age = models.PositiveIntegerField(default=28, validators=[MinValueValidator(18), MaxValueValidator(60)])
    age = HTMLField(default=15)
    minimum_qualification = models.CharField(max_length=50, choices=QUALIFICATION)

    total_posts = models.PositiveIntegerField()
    application_fee = HTMLField(default="Not announced")
    # application_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    # .....
    fee_last_date = models.DateField(null=True, blank=True)
    correction_date = models.DateField(null=True, blank=True)
    exam_date = models.DateField(null=True, blank=True)
    # .....

    # .....
    # general_obc_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
    # sc_st_ph_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
    # female_fee = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000)])
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
    is_archived = models.BooleanField(default=False, verbose_name="Archived?")

    created_on = models.DateField(auto_now_add=True, editable=False)
    updated_on = models.DateField(auto_now=True)

    slug = models.SlugField(max_length=300, blank=True, null=True, default='')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        get_latest_by = 'created_on'
        ordering=['-created_on']


    def __str__(self):
        return self.post_title


    def save(self, *args, **kwargs):
        if not self.slug and self.post_title:
            self.slug = slugify(self.post_title + "  " + str(self.state) + " " + str(self.total_posts))
        if self.image:
            picture = self.image
            if picture.size > 0.1*1024*1024:
                self.image = compress(picture)
        return super(Job, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('jobs:jobDetail', kwargs={"slug": self.slug})


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'jpeg', quality=50, optimize=True)
    new_image = File(im_io, name=image.name)
    im.close()
    return new_image
