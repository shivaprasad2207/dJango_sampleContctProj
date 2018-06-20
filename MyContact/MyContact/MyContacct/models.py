from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class BookContact(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=255, blank=True)
    firstName = models.CharField(max_length=255, blank=True)
    lastName = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    contactAdress = models.CharField(max_length=255, blank=True)
    is_active = models.IntegerField(default=1)