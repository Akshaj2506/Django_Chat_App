from django.urls import re_path
from chat_app.consumers import ChatConsumer

WebSocketUrlPatterns = [
   re_path(r'ws/chat/(?P<user_id>\d+)/$', ChatConsumer.as_asgi()),
]