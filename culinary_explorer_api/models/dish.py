from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    notes = models.CharField(max_length=100)
    food_image_url = models.TextField(default='https://example.com/default-image.jpg')
    price = models.CharField(max_length=100)