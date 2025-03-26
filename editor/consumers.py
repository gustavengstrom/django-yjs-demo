from logging import getLogger
from typing import TypedDict
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.generic.websocket import AsyncWebsocketConsumer  # type: ignore[import-not-found]
from pycrdt import (
    Doc,
    Text,
    Awareness,
    YMessageType,
    YSyncMessageType,
    read_message,
    handle_sync_message,
    create_update_message,
    create_sync_message,
    create_awareness_message,
)
from pycrdt_websocket.websocket import Websocket
from pycrdt_websocket.django_channels_consumer import YjsConsumer

logger = getLogger(__name__)


class CustomYjsConsumer(YjsConsumer):
    """A working consumer for [Django Channels](https://github.com/django/channels)."""

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data is None:
            return
        print("(1) ydoc.get", self.ydoc.get("editor", type=Text))
        await self.group_send_message(bytes_data)

        if bytes_data[0] == 2:
            self.ydoc.apply_update(bytes_data)
            print("(2) ydoc.get", self.ydoc.get("editor", type=Text))
        print(
            text_data,
            bytes_data[0],
            bytes_data[:],
            YSyncMessageType.SYNC_STEP1,
            YSyncMessageType.SYNC_STEP2,
            YSyncMessageType.SYNC_UPDATE,
            YMessageType.SYNC,
        )
        if bytes_data[0] != YMessageType.SYNC:
            return
        logger.debug(
            "Received %s message from endpoint: %s",
            YSyncMessageType(bytes_data[1]).name,
            self._websocket_shim.path,
        )
        reply = handle_sync_message(bytes_data[1:], self.ydoc)
        if reply is not None:
            logger.debug(
                "Sending %s message to endpoint: %s",
                YSyncMessageType.SYNC_STEP2.name,
                self._websocket_shim.path,
            )
            await self._websocket_shim.send(reply)
