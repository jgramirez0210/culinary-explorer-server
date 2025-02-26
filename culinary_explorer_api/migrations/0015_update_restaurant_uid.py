# Generated by Django 4.2.13 on 2025-02-26 20:14

from django.db import migrations

def update_restaurant_uid(apps, schema_editor):
    Restaurants = apps.get_model('culinary_explorer_api', 'Restaurants')
    User = apps.get_model('culinary_explorer_api', 'User')
    try:
        new_user = User.objects.get(uid='aPkqPWh2qYXzL2OHlFunih1ZR3U2')
        Restaurants.objects.all().update(uid=new_user.uid)
    except User.DoesNotExist:
        pass

class Migration(migrations.Migration):

    dependencies = [
        ('culinary_explorer_api', '0014_alter_restaurants_uid'),
    ]

    operations = [
        migrations.RunPython(update_restaurant_uid),
    ]
