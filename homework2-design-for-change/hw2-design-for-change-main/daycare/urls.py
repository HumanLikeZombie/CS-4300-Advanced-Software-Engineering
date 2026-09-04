from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("feed/<int:dragon_id>/", views.feed_puff, name="feed_puff"),
]
