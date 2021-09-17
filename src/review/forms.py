from django import forms
from .models import Ticket, Review


class NewTicketForm(forms.ModelForm):
    title = forms.CharField(label='titre')

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class NewReviewForm(forms.ModelForm):
    choices = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    body = forms.CharField(label='critique', widget=forms.Textarea, max_length=8192)
    headline = forms.CharField(label='titre')
    rating = forms.TypedChoiceField(label='note',widget=forms.RadioSelect(), choices=choices, coerce=int)

    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']


