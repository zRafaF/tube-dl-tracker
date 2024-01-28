# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pydantic import BaseModel, Field
from enum import Enum


class PagesBase(BaseModel):
    name: str = Field(..., example="home")
    url: str = Field(..., example="/")


class MessageType(str, Enum):
    PRIMARY = "primary"
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"


class MessagesBase(BaseModel):
    title: str = Field(..., example="Algo deu errado...")
    type: MessageType = Field(..., example=MessageType.DANGER)
    id: int = Field(..., example=1)


class GlobalsBase(BaseModel):
    pages: list[PagesBase] = (
        Field(
            ...,
            example=[
                {"name": "home", "url": ""},
                {"name": "items", "url": "items/1"},
                {"name": "settings", "url": "settings"},
            ],
        ),
    )
    messages: list[MessagesBase] = []
    base_url: str = Field(..., example="/")
