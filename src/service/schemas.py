# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pydantic import BaseModel, Field


class PagesBase(BaseModel):
    name: str = Field(..., example="home")
    url: str = Field(..., example="/")


class GlobalsBase(BaseModel):
    pages: list[PagesBase] = Field(
        ...,
        example=[
            {"name": "home", "url": "/"},
            {"name": "items", "url": "items/1"},
            {"name": "settings", "url": "/settings"},
        ],
    )
