from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    profile_image_url = models.CharField(max_length=255)
    uid = models.CharField(max_length=50)
