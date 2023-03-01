import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddleware, AuthMiddlewareStack

import socialNet.apps.network.routing as routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialNet.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})
