from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField



STATUS = ((0, "Draft"), (1, "Published"))

# Rating from 0 to 5
RATING = [(i,i) for i in range(6)]

# Create your models here.

class Movie(models.Model):
    """
    Description needed
    """
    movie_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movie_posts"
    )
    genre = models.ManyToManyField(
        'Genre', related_name="genres"
    )
    country = CountryField()  # Installed according to https://pypi.org/project/django-countries/
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
    # image
    # average_rating = models.IntegerField? does not need to be here as it is collected from reviews, doe snot need to be stored here?
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return self.movie_title

# function to conditionalise the dafult value of approved
# def default_approved():
#     if not (Review.text and Review.title):
#         return True
#     else:
#         return False


class Review(models.Model):
    """
    Description
    """
     

    title = models.CharField(max_length=200, blank=True)
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
    # total_likes = IntegerField?
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
    