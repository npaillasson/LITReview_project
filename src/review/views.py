from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewTicketForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.views.generic import DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import NewTicketForm, NewFollowedUser
from .models import UserFollows

@login_required
def index(request):
    section = "flux"
    return render(request, 'review/index.html', {'page': request.path, 'section': section})

@login_required()
def new_ticket(request):

    if request.method == 'POST':
        form = NewTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.image = form.cleaned_data.get('image')
            ticket.user = request.user
            ticket.save()
            return redirect('review:index')
    else:
        form = NewTicketForm
    return render(request, 'review/new_ticket.html', {'form': form, 'page': request.path})

@login_required()
def subscription_page(request):

    section = 'subscription'

    return render(request, 'review/subscriptions.html', {'section': section,
                                                         'list_of_following_users': request.user.following.all(),
                                                         'list_of_followed_users': request.user.following_by.all()})

@login_required()
def new_follow(request, username):
    print(username)
    user_follow = User.objects.filter(username=username).first()
    if user_follow:
        if user_follow == request.user:
            return redirect('review:subscription_page')
        else:
            NewFollowedUser = UserFollows()
            NewFollowedUser.user = request.user
            NewFollowedUser.followed_user = user_follow
            try:
                NewFollowedUser.save()
            except:
                pass
            return redirect('review:subscription_page')


@method_decorator(login_required, name='dispatch')
class DeleteSubscription(DeleteView):
    model = UserFollows
    success_url = reverse_lazy('review:subscription_page')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
