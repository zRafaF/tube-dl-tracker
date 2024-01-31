# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from config.schemas import QualityPresetsBase
from .schemas import GlobalsBase, PagesBase
from importlib.metadata import version

GLOBALS = GlobalsBase(
    pages=[
        PagesBase(name="Home", url="", on_navbar=True),
        PagesBase(name="Add Playlist", url="add-playlist"),
        PagesBase(name="Settings", url="settings", on_navbar=True),
    ],
    messages=[],
    base_url="/",
    demo_mode=False,
    app_version="0.1.0",
    yt_dlp_version=version("yt_dlp"),
    availableQualities=list(QualityPresetsBase.__members__.values()),
)
