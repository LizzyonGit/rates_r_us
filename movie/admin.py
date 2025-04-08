from django.contrib import admin
from .models import Movie, Review, Actor, Director

# From https://stackoverflow.com/questions/14828168/django-show-filter-horizontal-on-user-change-admin-page
class ActorFilter(admin.ModelAdmin):
    filter_horizontal = ('cast', )

# Register your models here.
admin.site.register(Movie, ActorFilter)
admin.site.register(Review)
admin.site.register(Actor)
admin.site.register(Director)

