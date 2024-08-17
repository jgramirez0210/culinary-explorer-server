from django.db import models
from .food_log import food_log
from .categories import categories


class Categories(models.Model):

    food_id = models.ForeignKey(food_log, on_delete=models.CASCADE)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)