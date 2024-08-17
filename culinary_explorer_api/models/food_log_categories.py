from django.db import models
from .food_log import Food_Log
from .categories import Categories


class FoodLogCategories(models.Model):

    food_id = models.ForeignKey(Food_Log, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)