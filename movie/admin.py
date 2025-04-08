from django.contrib import admin
from .models import Movie, Review, Actor, Director

# From https://stackoverflow.com/questions/14828168/django-show-filter-horizontal-on-user-change-admin-page
# From https://stackoverflow.com/questions/73570167/django-filter-horizontal-how-to-connect-more-fields-together



class HorizontalFilter(admin.ModelAdmin):
    """
    Adds an extra filter to the cast, directed_by and genre field
    """
    filter_horizontal = ['cast', 'directed_by', 'genre']

# Register your models here.
admin.site.register(Movie, HorizontalFilter)
admin.site.register(Review)
admin.site.register(Actor)
admin.site.register(Director)

