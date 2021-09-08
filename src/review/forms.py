from django import forms
from .models import Ticket, UserFollows


class NewTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class NewFollowedUser(forms.ModelForm):

    #def __init__(self, selection):
    #    forms.ModelForm.__init__(self)
    #    self.choices = selection


    #followed_user = forms.ChoiceField(widget=forms.Select(self.choices))

    class Meta:
        model = UserFollows
        fields = ['followed_user']