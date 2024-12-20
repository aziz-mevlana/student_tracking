# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.c_index, name="c_index"),
    path("<str:room_name>/", views.room, name="room"),
    path("start_chat/<str:username>", views.start_chat, name="start_chat"),
    path("widget_chat", views.widget_chat, name="widget_chat")
]