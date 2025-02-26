# Generated by Django 4.2.13 on 2025-02-26 20:21

import culinary_explorer_api.models.restaurants
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('culinary_explorer_api', '0015_update_restaurant_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='uid',
            field=models.ForeignKey(default=culinary_explorer_api.models.restaurants.get_default_user, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL),
        ),
    ]
