from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
from django.views.generic import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.db import transaction
from .forms import NewTicketForm, NewReviewForm
from .models import UserFollows, Ticket, Review
from .review_functions import multi_request, review_already_exist, get_ticket_from_pk, \
    create_ticket_and_answer, create_ticket


@login_required
def index(request):
    section = "flux"
    posts_to_display = multi_request(feed=True, request=request)
    return render(request, 'review/index.html', {'ticket_button': True, 'section': section,
                                                 'posts_to_display': posts_to_display, 'range': range(5)})


@login_required
def posts(request):
    section = "posts"
    posts_to_display = multi_request(request=request)
    return render(request, 'review/index.html', {'ticket_button': True, 'section': section,
                                                 'posts_to_display': posts_to_display, 'range': range(5)})


@login_required()
def new_ticket(request):

    if request.method == 'POST':
        form = NewTicketForm(request.POST, request.FILES)
        if form.is_valid():
            create_ticket(request, form_ticket=form)
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
    user_follow = User.objects.get(username=request.POST.get("subscribe_to"))
    if user_follow:
        if user_follow == request.user:
            return redirect('review:subscription_page')
        else:
            new_followed_user = UserFollows()
            new_followed_user.user = request.user
            new_followed_user.followed_user = user_follow
            try:
                new_followed_user.save()
            except IntegrityError:
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
class CreateReview(CreateView):
    model = Review
    form_class = NewReviewForm
    success_url = reverse_lazy('review:index')
    template_name = 'review/new_review.html'
    context_object_name = 'review'

    def form_valid(self, form):
        review = form.save(commit=False)
        review.ticket = get_ticket_from_pk(self.kwargs['pk'])
        review.user = self.request.user
        review.save()
        return redirect('review:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_already_exist(self.kwargs['pk'])
        context['post'] = get_ticket_from_pk(self.kwargs['pk'])
        context['ticket_button'] = False
        context['page'] = 'new_review'
        return context


@method_decorator(login_required, name='dispatch')
class DeleteReview(DeleteView):
    model = Review
    success_url = reverse_lazy('review:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class EditReview(UpdateView):
    model = Review
    form_class = NewReviewForm
    template_name = 'review/new_review.html'

    def form_valid(self, form):
        review = form
        review.save()
        return redirect('review:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object.ticket
        context['ticket_button'] = False
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@transaction.atomic
def create_ticket_and_review(request):

    if request.method == 'POST':
        form_ticket = NewTicketForm(request.POST, request.FILES)
        form_review = NewReviewForm(request.POST)
        if form_ticket.is_valid() and form_review.is_valid():
            create_ticket_and_answer(request, form_ticket, form_review)
            return redirect('review:index')

    form_ticket = NewTicketForm()
    form_review = NewReviewForm()
    form_ticket_list = [form_ticket]
    form_review_list = [form_review]
    return render(request, 'review/new_ticket_and_review.html',
                  context={'form_ticket_list': form_ticket_list, 'form_review_list': form_review_list})
