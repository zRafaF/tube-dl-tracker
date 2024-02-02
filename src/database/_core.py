# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from ._const import DATABASE
from .models import Author, Comment, Thumbnail, Video, Playlist


class DataBase:
    def __init__(self):
        self.db = DATABASE

    def start(self):
        self.db.connect()
        self.db.create_tables([Author, Comment, Thumbnail, Video, Playlist])

    def add_author(self, name: str, thumb_path: str, yt_id: str):
        return Author.create(name=name, thumb_path=thumb_path, yt_id=yt_id)
