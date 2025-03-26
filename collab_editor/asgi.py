import os

from django.core.asgi import get_asgi_application

# Set the Django settings module and initialize Django first
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "collab_editor.settings")
django_asgi_app = get_asgi_application()

# Import these after Django is initialized
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from editor import routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
