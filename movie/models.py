from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

MOVIE_GENRE = (
    ('1', 'Action'),
    ('2', 'Adventure'),
    ('3', 'Animation'),
    ('4', 'Comedy'),
    ('5', 'Crime'),
    ('6', 'Thriller'),
    ('7', 'Documentary'),
    ('8', 'Drama'),
    ('9', 'Fantasy'),
    ('10', 'Horror'),
    ('11', 'Musical'),
    ('12', 'Mystery'),
    ('13', 'Romance'),
    ('14', 'Science fiction'),
    ('15', 'War'),
    ('16', 'Western')
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
    )
    genre = models.CharField(choices=MOVIE_GENRE)
    country = CountryField()  # Installed according to https://pypi.org/project/django-countries/
    release_date = models.DateField()  # Datepicker shows when debug is True
    status = models.IntegerField(choices=STATUS, default=0)
    # actors = new actors model
    # directed_by = director model?
    plot = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # image
    # excerpt maybe not needed
    # average_rating = models.IntegerField?



