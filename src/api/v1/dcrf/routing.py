from django.urls import path

from src.api.v1.dcrf.chats.consumers import chat as consumers


websocket_urlpatterns = [
    path("ws/", consumers.UserConsumer.as_asgi()),
    path('ws/chat/', consumers.RoomConsumer.as_asgi()),
]