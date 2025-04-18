# Generated by Django 4.2.20 on 2025-04-17 10:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_alter_review_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
