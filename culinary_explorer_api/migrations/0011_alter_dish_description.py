# Generated by Django 4.2.14 on 2024-08-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinary_explorer_api', '0010_rename_dish_id_food_log_dish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
