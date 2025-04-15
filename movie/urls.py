from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('', views.MovieList.as_view(), name='home'),
]