# Generated by Django 4.2.13 on 2024-08-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinary_explorer_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]