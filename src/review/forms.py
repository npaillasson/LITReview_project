from django import forms
from .models import Ticket, UserFollows


class NewTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class NewFollowedUser(forms.ModelForm):
    followed_user = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 1}))

    class Meta:
        model = UserFollows
        fields = ['followed_user']