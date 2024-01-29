# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pydantic import BaseModel, Field
from typing import Optional, List


class RawExtractedCommentBase(BaseModel):
    text: Optional[str] = Field(None)
    parent: Optional[str] = Field(None)
    like_count: Optional[int] = Field(None)
    author: Optional[str] = Field(None)
    author_thumbnail: Optional[str] = Field(None)
    author_url: Optional[str] = Field(None)


class RawExtractedThumbnailBase(BaseModel):
    url: Optional[str] = Field(None)
    width: Optional[int] = Field(None)
    height: Optional[int] = Field(None)


class RawExtractedPlaylistVideoBase(BaseModel):
    id: Optional[str] = Field(None)
    title: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    uploader: Optional[str] = Field(None)
    uploader_id: Optional[str] = Field(None)
    uploader_url: Optional[str] = Field(None)
    duration: Optional[int] = Field(None)
    view_count: Optional[int] = Field(None)
    thumbnails: Optional[List[RawExtractedThumbnailBase]] = Field(None)


class RawExtractedPlaylistBase(BaseModel):
    id: Optional[str] = Field(None)
    title: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    thumbnails: Optional[List[RawExtractedThumbnailBase]] = Field(None)
    description: Optional[str] = Field(None)
    videos: Optional[List[RawExtractedPlaylistVideoBase]] = Field(None)
    uploader: Optional[str] = Field(None)
    uploader_id: Optional[str] = Field(None)
    uploader_url: Optional[str] = Field(None)
    view_count: Optional[int] = Field(None)
    tags: Optional[List[str]] = Field(None)


class RawExtractedVideoBase(BaseModel):
    id: Optional[str] = Field(None)
    title: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    uploader: Optional[str] = Field(None)
    uploader_id: Optional[str] = Field(None)
    uploader_url: Optional[str] = Field(None)
    view_count: Optional[int] = Field(None)
    comments: Optional[List[RawExtractedCommentBase]] = Field(None)
    duration: Optional[int] = Field(None)
    width: Optional[int] = Field(None)
    height: Optional[int] = Field(None)
    categories: Optional[List[str]] = Field(None)
    tags: Optional[List[str]] = Field(None)
