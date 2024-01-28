# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from .schemas import GlobalsBase, PagesBase


GLOBALS = GlobalsBase(
    pages=[
        PagesBase(name="home", url="/"),
        PagesBase(name="items", url="/items/1"),
        PagesBase(name="settings", url="/settings"),
    ],
    messages=[],
)
