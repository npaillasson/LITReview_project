from operator import attrgetter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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