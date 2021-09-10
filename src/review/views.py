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
    if request.method == 'POST':
        followed_user = dict(request.POST)["followed_user"][0]
        followed_user = User.objects.filter(username=followed_user).first()
        print(followed_user.id)
        form = NewFollowedUser()
        form.followed_user = followed_user.id
        print('this is form',form)
        #user_follow = form.save(commit=False)
        #user_follow.followed_user = followed_user
        #print(user_follow.__dict__)
        #print(type('azazaz', type(form.followed_user)))
        if form.is_valid():
            user_follow = form.save(commit=False)
            user_follow.user = request.user
            if user_follow.user != user_follow.followed_user:
                user_follow.save()
            return redirect('review:subscription_page')
    else:
        form = NewFollowedUser()

    return render(request, 'review/subscriptions.html', {'form': form, 'section': section,
                                                         'list_of_following_users': request.user.following.all(),
                                                         'list_of_followed_users': request.user.following_by.all()})

@method_decorator(login_required, name='dispatch')
class DeleteSubscription(DeleteView):
    model = UserFollows
    success_url = reverse_lazy('review:subscription_page')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class DeleteSubscription(CreateView):
    model = UserFollows
    form_class = NewFollowedUser
    success_url = reverse_lazy('review:subscription_page')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)