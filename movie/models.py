from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class Post(models.Model):
    MOVIE_GENRE = {
        '1': 'Mystery',
        '2': 'Comedy',
        '3': 'Thriller',
    }
    movie_title = models.CharField(max_length=200, unique=True)
    genre = models.CharField(max_length=3, choices=MOVIE_GENRE)
    country = CountryField()
