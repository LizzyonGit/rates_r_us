from django.shortcuts import render
from django.views import generic
from .models import Movie

# Create your views here.
class MovieList(generic.ListView):
    """
    Filters on published movie posts
    """
    queryset = Movie.objects.all().filter(status=1)


    


