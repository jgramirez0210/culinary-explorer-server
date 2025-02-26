from django.db import models

class Restaurants(models.Model):
    restaurant_name = models.CharField(max_length=100)
    restaurant_address = models.CharField(max_length=100)
    website_url = models.CharField(max_length=100)
    uid = models.CharField(max_length=50, default='default_user')