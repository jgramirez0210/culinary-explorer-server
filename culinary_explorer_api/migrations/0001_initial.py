# Generated by Django 4.2.14 on 2024-08-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=50)),
                ('profile_image_url', models.CharField(max_length=255)),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
    ]
