from django.apps import AppConfig


class MovieConfig(AppConfig):
    """
    Provides primary key type for movie app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie'
