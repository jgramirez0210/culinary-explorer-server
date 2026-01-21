from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Django's AbstractUser already includes:
    # - first_name, last_name, email (as username/email fields)
    # - password, last_login, date_joined, etc.

    # Add your custom fields
    profile_image_url = models.CharField(max_length=255, blank=True)
    uid = models.CharField(max_length=50, unique=True)

    # Specify which field to use as username (since we're not using Django's default username)
    # We'll use uid as the unique identifier
    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
