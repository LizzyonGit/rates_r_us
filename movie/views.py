from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Movie, Review
from .forms import ReviewForm


# Create your views here.
class MovieList(generic.ListView):
    """
    Filters on published movie posts
    """
    model = Movie
    template_name = "movie/index.html"
    # From https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view (post by Pran Kumar Sarkar)
    context_object_name = 'movies'
    #paginate_by = 9

    def get_queryset(self): 
        queryset = {'published_movies': Movie.objects.all().filter(status=1),
        'top_picks': Movie.objects.all().filter(top_pick=True)[:3]
        }
        return queryset 


    




# Followed tutorial https://learndjango.com/tutorials/django-search-tutorial and django doc for search functionality
# Help from https://forum.djangoproject.com/t/find-objects-with-mix-distinct-and-order-by/13010, https://stackoverflow.com/questions/73164250/find-unique-values-in-django/73164902, django doc
class SearchResultsView(generic.ListView):
    """
    Seach page
    """
    model = Movie
    template_name = 'movie/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Movie.objects.filter(
            Q(movie_title__icontains=query) | Q(cast__name__icontains=query) | Q(directed_by__name__icontains=query)
            ).order_by('movie_title').distinct('movie_title')
        return object_list


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
    # approved_reviews = movie.reviews.filter(approved=True)
    

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


    review_form = ReviewForm()
    
    return render(
        request,
        "movie/movie_detail.html",
        {
            "movie": movie,
            "reviews": reviews,
            #"review_count": review_count,
            "review_form": review_form,
            #"average_rating": average_rating,
            # "approved_reviews": approved_reviews,
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

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.movie = movie
            # Sets approved to True if text and title are empty in the updated review, message is different for both situations
            if not review.text and not review.title:
                review.approved = True
                review.save()
                messages.add_message(request, messages.SUCCESS, 'Review updated and published')
            else:
                review.approved = False
                review.save()
                messages.add_message(request, messages.SUCCESS, 'Review updated and awaiting approval')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review')

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))

def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews')

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))