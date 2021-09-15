from django import forms
from .models import Ticket, Review


class NewTicketForm(forms.ModelForm):


    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class NewReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']
