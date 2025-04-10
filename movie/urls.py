from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('', views.MovieList.as_view(), name='home'),
]