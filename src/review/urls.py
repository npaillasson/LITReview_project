from django.urls import path, re_path
from .views import index, new_ticket, subscription_page, DeleteSubscription, new_follow, posts, new_review, EditTicket, DeleteTicket
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('posts', posts, name='posts'),
    path('new_review', new_review, name='new_review'),
    path('update_ticket/<int:pk>/', EditTicket.as_view(), name='edit_ticket'),
    path('delete_ticket/<int:pk>/', DeleteTicket.as_view(), name='delete_ticket'),
    path('new_ticket/', new_ticket, name='new_ticket'),
    path('ticket_change/', new_ticket, name='ticket_change'),
    path('subscription/', subscription_page, name='subscription_page'),
    path(r'subscription/add/', new_follow, name='new_follow'),
    path("subscription/<int:pk>/delete_subscription/", DeleteSubscription.as_view(), name='delete_subscription')
]

