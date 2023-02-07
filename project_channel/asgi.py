"""
ASGI config for project_channel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# add this
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app_channel import consumers


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_channel.settings")

application = get_asgi_application()


ws_patterns = [
    path("ws/test", consumers.TestConsumer.as_asgi()),
    path("ws/new", consumers.NewConsumer.as_asgi()),
]

application = ProtocolTypeRouter({"websocket": URLRouter(ws_patterns)})
