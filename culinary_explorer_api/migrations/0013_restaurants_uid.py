# Generated by Django 4.2.16 on 2025-02-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinary_explorer_api', '0012_alter_dish_food_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='uid',
            field=models.CharField(default='aPkqPWh2qYXzL2OHlFunih1ZR3U2', max_length=50),
        ),
    ]
