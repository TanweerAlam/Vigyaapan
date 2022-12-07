from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    GENDER = [
        ('male', _('Male')),
        ('female', _('Female')),
        ('other', _('Other'))
    ]
    gender = models.CharField(max_length=10, choices=GENDER)

    # USERNAME_FIELD = 'email'