"""
ASGI config for Chat_Application project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat_Application.settings')

asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
   "http" : asgi_app
})
ASGI_APPLICATION = 'Chat_Application.asgi.application'