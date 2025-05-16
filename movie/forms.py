from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    Form class for users to leave a review.
    """
    class Meta:
        """
        Specify the model and available fields.
        """
        model = Review
        fields = ('rating', 'title', 'text')
