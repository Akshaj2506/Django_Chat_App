from django.urls import path
from chat_app.consumers import ChatConsumer

WebSocketUrlPatterns = [
   path('ws/chat/<int:user_id>/', ChatConsumer.as_asgi()),
]