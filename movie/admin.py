from django.contrib import admin
from .models import Movie, Review, Actor, Director, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):
    """
    Adds displayed fields in list, which fields can be searched, filter and
    prepopulated slug when writing post.
    Slug is title + release date in case of movies with same name.
    filter_horizontal adds an extra filter to the cast, directed_by and genre
    field so it is easier to select from large lists.
    Implements summernote field.

    """

    list_display = ('movie_title', 'created_on', 'release_date', 'status')
    # cast__name searches on actor names as cast is manytomany field
    search_fields = ['movie_title', 'cast__name']
    list_filter = ('status', 'top_pick')
    prepopulated_fields = {'slug': ('movie_title', 'release_date')}
    filter_horizontal = ['cast', 'directed_by', 'genre']
    summernote_fields = ('plot',)  # works when debug is true

# Filter_horizontal sources:
# https://stackoverflow.com/questions/14828168/django-show-filter-horizontal-on-user-change-admin-page
# https://stackoverflow.com/questions/73570167/django-filter-horizontal-how-to-connect-more-fields-together

# Search many-to-many field source:
# https://stackoverflow.com/questions/51931762/how-can-we-search-many-to-many-field-in-django-admin-search-field


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Adds fields to table and adds filter.
    """
    list_display = ('title', 'rating', 'movie', 'approved', 'created_on')
    # Code below so you can search on movie title in search field (django doc)
    search_fields = ['movie__movie_title']
    list_filter = ('approved', 'rating')


# Registers the models

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
