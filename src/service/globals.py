# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from .schemas import GlobalsBase, PagesBase


GLOBALS = GlobalsBase(
    pages=[
        PagesBase(name="Home", url=""),
        PagesBase(name="Add Playlist", url="add-playlist"),
        PagesBase(name="Settings", url="settings"),
    ],
    messages=[],
    base_url="/",
)
