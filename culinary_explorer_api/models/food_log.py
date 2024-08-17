from django.db import models
from .food_log import food_log


class Food_Log(models.Model):

    restaurant_id = models.CharField(max_length=100)
    dish_id = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    food_image = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)
