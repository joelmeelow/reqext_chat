import os
import django
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dre.settings')

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django.setup()  # This is crucial to avoid the AppRegistryNotReady error

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

# Import your routing after setting up Django
from pharm_chat.routing import websocket_urlpatterns

# Initialize the Django ASGI application
django_asgi_app = get_asgi_application()

from pharm_chat.consumers import ChatRoomConsumer  # Move this after django.setup()

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        )
    ),
})
