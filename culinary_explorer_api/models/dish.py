from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    price = models.CharField(max_length=100)