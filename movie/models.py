from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

MOVIE_GENRE = (
        ('1', 'Mystery'),
        ('2', 'Comedy'),
        ('3', 'Thriller')
    )

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    """
    Description needed
    """
    movie_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movie_posts"
    )  # no cascade on delete because author is less important
    genre = models.CharField(max_length=3, choices=MOVIE_GENRE)
    country = CountryField()  # Installed according to https://pypi.org/project/django-countries/
    release_date = models.DateField()
    status = models.IntegerField(choices=STATUS, default=0)

