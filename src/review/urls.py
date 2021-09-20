from django.urls import path, re_path
from .views import index, new_ticket, subscription_page, DeleteSubscription, new_follow,\
    posts, EditTicket, DeleteTicket, CreateReview, DeleteReview, EditReview, create_ticket_and_review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('posts', posts, name='posts'),
    path('update_ticket/<int:pk>/', EditTicket.as_view(), name='edit_ticket'),
    path('new_ticket/', new_ticket, name='new_ticket'),
    path('delete_ticket/<int:pk>/', DeleteTicket.as_view(), name='delete_ticket'),
    path('answer_ticket/<int:pk>/', CreateReview.as_view(), name='creation_review'),
    path('delete_review/<int:pk>/', DeleteReview.as_view(), name='delete_review'),
    path('update_review/<int:pk>/', EditReview.as_view(), name='update_review'),
    path('create_ticket_and_review/', create_ticket_and_review, name='create_ticket_and_review'),
    path('subscription/', subscription_page, name='subscription_page'),
    path(r'subscription/add/', new_follow, name='new_follow'),
    path("subscription/<int:pk>/delete_subscription/", DeleteSubscription.as_view(), name='delete_subscription')
]

