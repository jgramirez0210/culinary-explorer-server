# Generated by Django 4.2.14 on 2024-08-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinary_explorer_api', '0008_alter_food_log_dish_id_alter_food_log_restaurant_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_log',
            name='uid',
            field=models.CharField(max_length=50),
        ),
    ]
