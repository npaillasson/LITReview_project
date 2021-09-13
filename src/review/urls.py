from django.urls import path, re_path
from .views import index, new_ticket, subscription_page, DeleteSubscription, new_follow

urlpatterns = [
    path('', index, name='index'),
    path('new_ticket/', new_ticket, name='new_ticket'),
    path('ticket_change/', new_ticket, name='ticket_change'),
    path('subscription/', subscription_page, name='subscription_page'),
    path('subscription/<username>/', new_follow, name='new_follow'),
    path("subscription/<pk>/delete_subscription/", DeleteSubscription.as_view(), name='delete_subscription')
]

