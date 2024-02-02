# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from peewee import (
    Model,
    CharField,
    TextField,
    BooleanField,
    ForeignKeyField,
    IntegerField,
    DateTimeField,
)
import datetime
from ._const import DATABASE


class BaseModel(Model):
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Author(BaseModel):
    name = TextField()
    thumb_path = TextField()
    yt_id = CharField(unique=True)


class Comment(BaseModel):
    yt_id = TextField(unique=True)
    parent = TextField()
    text = TextField()
    author = ForeignKeyField(Author, backref="comments")
    like_count = IntegerField()


class Thumbnail(BaseModel):
    path = TextField()
    width = IntegerField()
    height = IntegerField()


class Video(BaseModel):
    title = TextField()
    author = ForeignKeyField(Author, backref="videos")
    yt_id = CharField(unique=True)
    original_url = TextField()
    description = TextField()
    path = TextField()
    thumbnail = ForeignKeyField(Thumbnail, backref="videos")
    view_count = IntegerField()
    height = IntegerField()
    width = IntegerField()
    duration = IntegerField()
    tags = TextField()
    categories = TextField()
    available = BooleanField()


class Playlist(BaseModel):
    title = TextField()
    author = ForeignKeyField(Author, backref="playlists")
    description = TextField()
    view_count = IntegerField()
    yt_id = CharField(unique=True)
    original_url = TextField()
    thumbnail = ForeignKeyField(Thumbnail, backref="playlists")
