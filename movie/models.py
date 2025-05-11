from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField
from django.db.models import Avg

# Status variable
STATUS = ((0, "Draft"), (1, "Published"))

# Rating from 0 to 5
RATING = [(i, i) for i in range(6)]

# Models


class Movie(models.Model):
    """
    Description needed
    """
    movie_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movie_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    genre = models.ManyToManyField(
        'Genre', related_name="genres"
    )
    country = CountryField()  # From https://pypi.org/project/django-countries/
    release_date = models.DateField()  # Datepicker shows when debug is True
    status = models.IntegerField(choices=STATUS, default=0)
    cast = models.ManyToManyField(
        'Actor', related_name="actors"
    )  # model name in quote because it's under it
    directed_by = models.ManyToManyField(
        'Director', related_name="directors"
    )
    plot = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    top_pick = models.BooleanField(default=False)
    pick_motivation = models.TextField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.movie_title

    # Two methods for displaying average rating when there are approved reviews
    # Calculate average rating of approved reviews.
    # Inspired by https://stackoverflow.com/questions/55325723/generate-average-for-ratings-in-django-models-and-return-with-other-model

    def approved_reviews(self):
        return self.reviews.filter(approved=True)

    def get_average_rating(self):
        average_rating = (self.approved_reviews().aggregate(Avg('rating'))
                          .get('rating__avg'))
        return average_rating


class Review(models.Model):
    """
    Description
    """

    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    text = models.TextField(max_length=2000, blank=True)
    approved = models.BooleanField(default=False)
    rating = models.IntegerField(choices=RATING)
    created_on = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="reviews"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'{self.title}'


class Actor(models.Model):
    """
    Descr
    """
    name = models.CharField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Director(models.Model):
    """
    Descr
    """
    name = models.CharField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Descr
    """
    type = models.CharField()

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return self.type
