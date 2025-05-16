from . import views
from django.urls import path

urlpatterns = [
    path('', views.MovieList.as_view(), name='home'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("my_reviews/", views.my_reviews, name="my_reviews"),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]
