from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Movie, Review
from .forms import ReviewForm


class MovieList(generic.ListView):
    """
    Returns all published movies and
    displayes them in a page of 3.
    **Context**

    ``queryset``
        All published instances of :model:`movie.Movie`.
    ``paginate_by``
        Number of movies per page.

    **Template**

    :template:`movie/index.html`
    """
    model = Movie
    template_name = "movie/index.html"
    queryset = Movie.objects.all().filter(status=1)
    paginate_by = 3

    # Below method needed to get pagination on first page for all movies,
    # because of Top pic section on first page. Sources:
    # https://stackoverflow.com/questions/60560493/django-listview-pagination-when-passing-multiple-objects-in-queryset
    # (post by Esmail Shabayek) and django docs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Picks 3 top picks (https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view (Pran Kumar Sarkar))
        context['top_picks'] = Movie.objects.all().filter(top_pick=True)[:3]
        return context


# Search functionality below from sources:
# Tutorial https://learndjango.com/tutorials/django-search-tutorial and django doc,
# https://forum.djangoproject.com/t/find-objects-with-mix-distinct-and-order-by/13010,
# https://stackoverflow.com/questions/73164250/find-unique-values-in-django/73164902
class SearchResultsView(generic.ListView):
    """
    Display movie result from user query in search field.

    **Context**

    ``object_list``
        All published movies for which the user query is included in
        the title, cast, and/or directors.
        (.distinct prevents duplicate results)

    **Template**
    :template:`movie/search_results.html`

    """
    model = Movie
    template_name = 'movie/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = (Movie.objects.filter(
            Q(movie_title__icontains=query) | Q(cast__name__icontains=query) |
            Q(directed_by__name__icontains=query),
            status=1).order_by('movie_title').distinct('movie_title'))
        return object_list


def movie_detail(request, slug):
    """
    Display an individual :model:`movie.Movie`.

    **Context**

    ``movie``
        An instance of :model:`movie.Movie`.
    ``reviews``
        All reviews related to the movie.
    ``review_form``
        An instance of :form:`movie.ReviewForm`

    **Template:**

    :template:`movie/movie_detail.html`
    """

    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    reviews = movie.reviews.all().order_by("-created_on")

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)

        # Check if there are any reviews posted by the user to raise error
        # https://stackoverflow.com/questions/46082573/django-forms-allow-logged-in-user-to-submit-only-one-comment-per-individual-pos
        user_reviews = movie.reviews.filter(author=request.user)

        if user_reviews:
            messages.add_message(request, messages.ERROR,
                                 'You have already reviewed this movie.')
            return HttpResponseRedirect(reverse('movie_detail', args=[slug]))

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.movie = movie
            # Following code sets approved to True if user only gives rating
            # and adapts message to it
            if not review.text and not review.title:
                review.approved = True
                review.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Thank you for your rating')
                # This updates the page after reviewing
                return HttpResponseRedirect(reverse
                                            ('movie_detail', args=[slug]))
            else:
                review.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Thank you for your review. '
                                     'It will be published after approval.')
                # This updates the page after reviewing
                return HttpResponseRedirect(reverse
                                            ('movie_detail', args=[slug]))

    review_form = ReviewForm()

    return render(
        request,
        "movie/movie_detail.html",
        {
            "movie": movie,
            "reviews": reviews,
            "review_form": review_form,
            },)


def review_edit(request, slug, review_id):
    """
    Display an individual review for edit.

    **Context**

    ``movie``
        An instance of :model:`movie.Movie`.
    ``review``
        A single review related to the movie.
    ``review_form``
        An instance of :form:`movie.ReviewForm`
    """
    if request.method == "POST":

        queryset = Movie.objects.filter(status=1)
        movie = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.movie = movie
            # Sets approved to True if text and title are empty
            # in the updated review, message is different for both situations
            if not review.text and not review.title:
                review.approved = True
                review.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Review updated and published')
            else:
                review.approved = False
                review.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Review updated and awaiting approval')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating review')

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    Delete an individual review.

    **Context**

    ``movie``
        An instance of :model:`movie.Movie`.
    ``review``
        A single review related to the movie.
    """
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own reviews')

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))


def my_reviews(request):
    """
    Display all reviews by one user

    **Context**

    ``my_reviews``
        All reviews by one user
    ``movies``
        All published movies

    **Template**

    :template:`movie/my_reviews.html`

    """
    queryset = Review.objects.all()
    my_reviews = queryset.filter(author=request.user).order_by("-created_on")
    movies = Movie.objects.filter(status=1)
    return render(
        request,
        "movie/my_reviews.html",
        {
            "my_reviews": my_reviews,
            "movies": movies,
         },
    )
