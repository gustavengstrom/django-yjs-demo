from django.urls import re_path, path

from . import consumers
from pycrdt_websocket.django_channels_consumer import YjsConsumer

websocket_urlpatterns = [
    # Use our custom consumer instead of the base YjsConsumer
    # path(r"ws/<str:room>", YjsConsumer.as_asgi()),
    path(r"ws/<str:room>", consumers.CustomYjsConsumer.as_asgi()),
]
