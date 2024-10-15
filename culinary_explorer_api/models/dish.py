from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    notes = models.CharField(max_length=100)
    food_image_url = models.URLField(max_length=500, default='https://example.com/default-image.jpg')  # Increased max_length
    price = models.CharField(max_length=100)