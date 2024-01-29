# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pydantic import BaseModel, Field
from enum import Enum


class PagesBase(BaseModel):
    name: str = Field(..., example="home")
    url: str = Field(..., example="/")
    on_navbar: bool = False


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
    pages: list[PagesBase] = Field(...)
    messages: list[MessagesBase] = []
    base_url: str = Field(..., example="/")
    demo_mode: bool = Field(..., example=True)
    app_version: str = Field(..., example="0.1.0")
    yt_dlp_version: str = Field(..., example="0.1.0")
