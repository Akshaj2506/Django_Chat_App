"""
ASGI config for Chat_Application project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

django_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat_app import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat_Application.settings')
application = ProtocolTypeRouter({
   "http" : django_app,
   "websocket" : AuthMiddlewareStack(
            URLRouter(routing.WebSocketUrlPatterns)
         )
})
ASGI_APPLICATION = 'Chat_Application.asgi.application'