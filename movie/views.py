from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.db.models import Avg
from .models import Movie
from .forms import ReviewForm


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
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.movie = movie
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )

    # calcualte average rating, need to fix display. Good it adds unapproved
    average_rating = reviews.aggregate(Avg('rating'))

    review_form = ReviewForm()
    

    return render(
        request,
        "movie/movie_detail.html",
        {
            "movie": movie,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
            "average_rating": average_rating,
         },
    )

