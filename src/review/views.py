from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewTicketForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.views.generic import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from operator import attrgetter
from .forms import NewTicketForm, NewReviewForm
from .models import UserFollows, Ticket, Review

@login_required
def index(request):
    section = "flux"
    followed_user = []
    followed_users_posts = []
    for user in request.user.following.all():
        followed_user.append(user.followed_user)
    posts_to_display = list(Ticket.objects.filter(user=request.user))
    posts_to_display.extend(list(Review.objects.filter(user=request.user)))
    for user in followed_user:
        followed_users_posts.extend(list(Ticket.objects.filter(user=user)))
        followed_users_posts.extend(list(Review.objects.filter(user=user)))
    posts_to_display.extend(followed_users_posts)
    posts_to_display.sort(key=attrgetter('time_created'), reverse=True)
    return render(request, 'review/index.html', {'page': request.path, 'section': section,
                                                 'posts_to_display': posts_to_display, 'range': range(5)})

@login_required
def posts(request):
    section = "posts"
    followed_user = []
    followed_users_tickets = []
    for user in request.user.following.all():
        followed_user.append(user.followed_user)
    tickets_to_display = list(Ticket.objects.filter(user=request.user))
    for user in followed_user:
        followed_users_tickets.extend(list(Ticket.objects.filter(user=user)))
    tickets_to_display.extend(followed_users_tickets)
    return render(request, 'review/index.html', {'page': request.path, 'section': section, 'ticket_to_display': tickets_to_display})

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
        form = NewTicketForm()
    return render(request, 'review/new_ticket.html', {'form': form, 'page': request.path})

@login_required()
def subscription_page(request):

    section = 'subscription'

    return render(request, 'review/subscriptions.html', {'section': section,
                                                         'list_of_following_users': request.user.following.all(),
                                                         'list_of_followed_users': request.user.following_by.all()})

@login_required()
def new_follow(request):
    user_follow = User.objects.get(username=request.GET.get("subscribe_to"))
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

@method_decorator(login_required, name='dispatch')
class EditTicket(UpdateView):
    model = Ticket
    fields = ('description', 'image', )
    template_name = 'review/new_ticket.html'

    def form_valid(self, form):
        ticket = form
        ticket.save()
        return redirect('review:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class DeleteTicket(DeleteView):
    model = Ticket
    success_url = reverse_lazy('review:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class CreationReview(CreateView):
    model = Review
    form_class = NewReviewForm
    success_url = reverse_lazy('review:index')
    template_name = 'review/new_review.html'
    context_object_name = 'review'


    def form_valid(self, form):
        review = form.save(commit=False)
        print(self.request.path)
        review.ticket = Ticket.objects.get(id=self.kwargs['pk'])
        review.user = self.request.user
        review.save()
        return redirect('review:index')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['post'] = Ticket.objects.get(id=self.kwargs['pk'])
        return context


@method_decorator(login_required, name='dispatch')
class DeleteReview(DeleteView):
    model = Review
    success_url = reverse_lazy('review:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class EditTicket(UpdateView):
    model = Review
    fields = ('headline', 'rating', 'body' )
    template_name = 'review/new_review.html'

    def form_valid(self, form):
        review = form
        review.save()
        return redirect('review:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
