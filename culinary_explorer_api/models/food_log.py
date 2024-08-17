from django.db import models
from .categories import Categories


class Food_Log(models.Model):
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    category = models.ManyToManyField(Categories)
    uid = models.CharField(max_length=50)