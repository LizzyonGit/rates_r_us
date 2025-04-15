from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Avg
from .models import Movie, Review
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
    approved_reviews = movie.reviews.filter(approved=True)
    review_count = approved_reviews.count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():            
            review = review_form.save(commit=False)
            review.author = request.user
            review.movie = movie
            # Following code sets approved to True if the user only gives a rating, and adapts message to it
            if not review.text and not review.title:
                review.approved = True
                review.save()
                messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your rating'
            )
            else:
                review.save()
                messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your review. It will be published after approval.'
            )

        

    # Calculate average rating of approved reviews. Inspired by https://stackoverflow.com/questions/55325723/generate-average-for-ratings-in-django-models-and-return-with-other-model
    average_rating = approved_reviews.aggregate(Avg('rating')).get('rating__avg')

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
            "approved_reviews": approved_reviews,
         },
    )

def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Movie.objects.filter(status=1)
        movie = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        # Need to check this for editing rating

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.movie = movie
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))