from django.urls import path
from cat_app.views.base import index_view, cat_view, feed_cat, play_cat, sleep_cat

urlpatterns = [
    path('', index_view),
    path('cat/', cat_view),
    path('cat/feed/', feed_cat),
    path('cat/play/', play_cat),
    path('cat/sleep/', sleep_cat),
]
