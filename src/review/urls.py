from django.urls import path
from .views import index, new_ticket, subscription_page, DeleteSubscription, new_follow,\
    posts, EditTicket, DeleteTicket, CreateReview, DeleteReview, EditReview, create_ticket_and_review

urlpatterns = [
    path('', index, name='index'),
    path('posts', posts, name='posts'),
    path('update_ticket/<int:pk>/', EditTicket.as_view(), name='edit_ticket'),
    path('new_ticket/', new_ticket, name='new_ticket'),
    path('delete_ticket/<int:ticket_pk>/', DeleteTicket.as_view(), name='delete_ticket'),
    path('answer_ticket/<int:ticket_pkpk>/', CreateReview.as_view(), name='creation_review'),
    path('delete_review/<int:review_pk>/', DeleteReview.as_view(), name='delete_review'),
    path('update_review/<int:review_pk>/', EditReview.as_view(), name='update_review'),
    path('create_ticket_and_review/', create_ticket_and_review, name='create_ticket_and_review'),
    path('subscription/', subscription_page, name='subscription_page'),
    path(r'subscription/add/', new_follow, name='new_follow'),
    path("subscription/<int:following_user_pk>/delete_subscription/", DeleteSubscription.as_view(), name='delete_subscription')
]

