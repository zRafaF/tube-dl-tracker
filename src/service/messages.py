# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .schemas import GlobalsBase, MessagesBase, MessageType
from .globals import GLOBALS
import asyncio


class Messenger:
    def __init__(self, globals: GlobalsBase):
        self._globals = globals
        self._last_message_id = 0

    async def _remove_message(self, message_id: int) -> None:
        await asyncio.sleep(2)
        for message in self._globals.messages:
            if message.id == message_id:
                self._globals.messages.remove(message)
                if len(self._globals.messages) == 0:
                    self._last_message_id = 0
                break

    def send_message(self, title: str, type: MessageType) -> None:
        current_message_id = self._last_message_id + 1
        message = MessagesBase(title=title, type=type, id=current_message_id)
        self._globals.messages.append(message)
        self._last_message_id = current_message_id
        asyncio.create_task(self._remove_message(current_message_id))


messenger = Messenger(GLOBALS)
