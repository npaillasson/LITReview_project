from operator import attrgetter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import NewTicketForm, NewReviewForm

def multi_request(request, feed=False):
    followed_user = []
    user_tickets = list(request.user.ticket_set.all())
    posts_list = list(user_tickets)
    for ticket in user_tickets:
        posts_list.extend(list(ticket.review_set.all()))
    posts_list.extend(list(request.user.review_set.all()))
    if feed:
        for user in request.user.following.all():
            followed_user.append(user.followed_user)
        for user in followed_user:
            posts_list.extend(list(user.ticket_set.all()))
            posts_list.extend(list(user.review_set.all()))
    posts_list = list(set(posts_list))
    posts_list.sort(key=attrgetter('time_created'), reverse=True)
    paginator_posts_list = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts_to_display = paginator_posts_list.page(page)
    except PageNotAnInteger:
        posts_to_display = paginator_posts_list.page(1)
    except EmptyPage:
        posts_to_display = paginator_posts_list.page(paginator_posts_list.num_pages)
    return posts_to_display

def review_already_exist(ticket_pk):
    ticket = get_ticket_from_pk(ticket_pk)
    if ticket.review_set.first():
        raise Http404


def get_ticket_from_pk(ticket_pk):
    return Ticket.objects.get(id=ticket_pk)


def create_ticket_and_answer(request, form_ticket, form_review):

    ticket = create_ticket(request, form_ticket)
    review = form_review.save(commit=False)
    review.ticket = ticket
    review.user = request.user
    review.save()
    return review


def create_ticket(request, form_ticket):

    ticket = form_ticket.save(commit=False)
    ticket.image = form_ticket.cleaned_data.get('image')
    ticket.user = request.user
    ticket.save()
    return ticket


