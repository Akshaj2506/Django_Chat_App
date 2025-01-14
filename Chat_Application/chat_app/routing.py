from django.urls import path, include
from chat_app.consumers import ChatConsumer

WebSocketUrlPatterns = [
   path("", ChatConsumer.as_asgi()),
]