from django.contrib import admin
from .models import Movie, Review, Actor, Director, Genre
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):
    """
    Adds displayed fields in list, which fields can be searched, filter and prepopulated slug when writing post
    filter_horizontal adds an extra filter to the cast, directed_by and genre field so 
    it is easier to select from large lists    
    Implements summernote field

    """

    list_display = ('movie_title', 'created_on', 'release_date', 'status')
    search_fields = ['movie_title', 'cast__name']  # cast_name searches on actor names as cast is manytomany field
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('movie_title',)}
    filter_horizontal = ['cast', 'directed_by', 'genre']    
    summernote_fields = ('plot',)  # works when debug is true



# From https://stackoverflow.com/questions/14828168/django-show-filter-horizontal-on-user-change-admin-page
# From https://stackoverflow.com/questions/73570167/django-filter-horizontal-how-to-connect-more-fields-together

# Search manytotmany: https://stackoverflow.com/questions/51931762/how-can-we-search-many-to-many-field-in-django-admin-search-field


# Register your models here.
admin.site.register(Review)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
