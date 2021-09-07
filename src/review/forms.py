from django import forms
from .models import Ticket


class NewTicketForm(forms.ModelForm):
    #message = forms.CharField(widget=forms.Textarea(), max_length=4000)
    #title = forms.CharField(max_length=128)
    #user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #image = forms.ImageField(null=True,)
    #time_created

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
