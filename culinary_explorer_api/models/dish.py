from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    food_image_url = models.URLField(default='https://example.com/default-image.jpg')
    price = models.CharField(max_length=100)