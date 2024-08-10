from django.db import models


class Categories(models.Model):

    category = models.CharField(max_length=50)
