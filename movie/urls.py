from . import views
from django.urls import path

urlpatterns = [
    path('', views.MovieList.as_view(), name='home'),
]