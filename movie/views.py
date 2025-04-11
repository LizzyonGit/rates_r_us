from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie

# Create your views here.
class MovieList(generic.ListView):
    """
    Filters on published movie posts
    """
    queryset = Movie.objects.all().filter(status=1)
    template_name = "movie/index.html"
    paginate_by = 4


def movie_detail(request, slug):
    """
    Display an individual :model:`movie.Movie`.

    **Context**

    ``movie``
        An instance of :model:`movie.Movie`.

    **Template:**

    :template:`movie/movie_detail.html`
    """

    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    reviews = movie.reviews.all().order_by("-created_on")
    review_count = movie.reviews.filter(approved=True).count()
    

    return render(
        request,
        "movie/movie_detail.html",
        {
            "movie": movie,
            "reviews": reviews,
            "review_count": review_count,
         },
    )

