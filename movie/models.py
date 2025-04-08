from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

MOVIE_GENRE = (
    (1, 'Action'),
    (2, 'Adventure'),
    (3, 'Animation'),
    (4, 'Comedy'),
    (5, 'Costume drama'),
    (6, 'Crime'),
    (7, 'Documentary'),
    (8, 'Drama'),
    (9, 'Fantasy'),
    (10, 'Horror'),
    (11, 'Musical'),
    (12, 'Mystery'),
    (13, 'Romance'),
    (14, 'Science fiction'),
    (15, 'Thriller'),
    (16, 'War'),
    (17, 'Western')
 )

STATUS = ((0, "Draft"), (1, "Published"))

RATING = [(i,i) for i in range(6)]

# Create your models here.

class Movie(models.Model):
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
    actors = models.ManyToManyField(
        'Actor', related_name="actors"
    )  # model name in quote because it's under it
    directed_by = models.ManyToManyField(
        'Director', related_name="directors"
    )
    plot = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # image
    # excerpt maybe not needed
    # average_rating = models.IntegerField?
    class Meta:
        ordering = ["-release_date"]
    def __str__(self):
        return self.title

class Review(models.Model):
    """
    Description
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    review = models.TextField(max_length=2000)
    approved = models.BooleanField(default=False)
    rating = models.IntegerField(choices=RATING)
    created_on = models.DateTimeField(auto_now_add=True)
    movie_post = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="reviews"
    )
    # total_likes = IntegerField?

class Actor(models.Model):
    """
    Descr
    """
    name = models.CharField()
    movie = models.ManyToManyField(
        Movie, related_name="movies"
    )

class Director(models.Model):
    """
    Descr
    """
    name = models.CharField()
    movie = models.ManyToManyField(
        Movie, related_name="movies"
    )
