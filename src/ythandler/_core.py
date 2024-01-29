# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from typing import Any, Tuple
from yt_dlp import YoutubeDL
from .raw_schemas import (
    RawExtractedThumbnailBase,
    RawExtractedPlaylistVideoBase,
    RawExtractedPlaylistBase,
    RawExtractedCommentBase,
    RawExtractedVideoBase,
)
import re
from functools import cache
from loguru import logger
import time
import asyncio


class YTHandler:
    def __init__(self):
        pass

    async def _invalidate_cache(self):
        await asyncio.sleep(60)
        self.get_playlist_info.cache_clear()
        self.get_video_info.cache_clear()

    @cache
    def get_playlist_info(
        self, playlist_id: str
    ) -> Tuple[RawExtractedPlaylistBase, float]:
        start = time.time()
        asyncio.create_task(self._invalidate_cache())

        ydl_opts = {"extract_flat": True, "verbose": True}
        with YoutubeDL(ydl_opts) as ydl:
            playlist_dict = ydl.extract_info(
                self.generate_playlist_url(playlist_id), download=False
            )
            extracted_playlist = self._extracted_playlist_dict_to_obj(playlist_dict)
            execution_time = time.time() - start
            logger.success(
                f"Fetched playlist data successfully, took {execution_time}s"
            )
            return (extracted_playlist, execution_time)

    @cache
    def get_video_info(
        self, video_id: str, max_comments: int = 10
    ) -> RawExtractedVideoBase:
        start = time.time()
        asyncio.create_task(self._invalidate_cache())
        ydl_opts = {
            "extract_flat": True,
            "verbose": True,
            "getcomments": True,
            "max_comments": max_comments,
        }
        with YoutubeDL(ydl_opts) as ydl:
            video_dict = ydl.extract_info(
                self.generate_video_url(video_id), download=False
            )
            extracted_video = self._extracted_video_dict_to_obj(video_dict)
            end = time.time()
            logger.success(f"Fetched video data successfully, took {end-start}s")
            return extracted_video

    def _extracted_playlist_dict_to_obj(
        self, extracted_playlist: dict[str, Any]
    ) -> RawExtractedPlaylistBase:
        for thumbnail in extracted_playlist.get("thumbnails"):
            playlist_thumbnails = [
                RawExtractedThumbnailBase(
                    url=thumbnail.get("url", ""),
                    width=thumbnail.get("width", -1),
                    height=thumbnail.get("height", -1),
                )
            ]

            playlist_videos = [
                RawExtractedPlaylistVideoBase(
                    id=video.get("id", ""),
                    title=video.get("title", "Empty"),
                    url=video.get("url", ""),
                    uploader=video["uploader"],
                    uploader_id=video["uploader_id"],
                    uploader_url=video["uploader_url"],
                    duration=video["duration"],
                    view_count=video["view_count"],
                    thumbnails=[
                        RawExtractedThumbnailBase(
                            url=thumbnail.get("url", ""),
                            width=thumbnail.get("width", -1),
                            height=thumbnail.get("height", -1),
                        )
                        for thumbnail in video.get("thumbnails")
                    ],
                )
                for video in extracted_playlist.get("entries")
            ]

        playlist = RawExtractedPlaylistBase(
            id=extracted_playlist.get("id", ""),
            title=extracted_playlist.get("title", "Empty"),
            url=extracted_playlist.get("webpage_url", ""),
            thumbnails=playlist_thumbnails,
            description=extracted_playlist.get("description", ""),
            videos=playlist_videos,
            uploader=extracted_playlist.get("uploader", "Empty"),
            uploader_id=extracted_playlist.get("uploader_id", ""),
            uploader_url=extracted_playlist.get("uploader_url", ""),
            view_count=extracted_playlist.get("view_count", -1),
            tags=extracted_playlist.get("tags", []),
        )
        return playlist

    def _extracted_video_dict_to_obj(
        self, extracted_video: dict[str, Any]
    ) -> RawExtractedVideoBase:
        video_comments = [
            RawExtractedCommentBase(
                text=comment.get("text", "Empty"),
                parent=comment.get("parent", "root"),
                like_count=comment.get("like_count", -1),
                author=comment.get("author", "Empty"),
                author_thumbnail=comment.get("author_thumbnail", ""),
                author_url=comment.get("author_url", ""),
            )
            for comment in extracted_video.get("comments")
        ]
        video = RawExtractedVideoBase(
            id=extracted_video.get("id"),
            title=extracted_video.get("title"),
            url=extracted_video.get("webpage_url"),
            description=extracted_video.get("description"),
            uploader=extracted_video.get("uploader"),
            uploader_id=extracted_video.get("uploader_id"),
            uploader_url=extracted_video.get("uploader_url"),
            view_count=extracted_video.get("view_count"),
            comments=video_comments,
            duration=extracted_video.get("duration", -1),
            width=extracted_video.get("width", -1),
            height=extracted_video.get("height", -1),
            categories=extracted_video.get("categories", []),
            tags=extracted_video.get("tags", []),
        )
        return video

    def generate_playlist_url(self, playlist_id: str) -> str:
        return f"https://www.youtube.com/playlist?list={playlist_id}"

    def generate_video_url(self, video_id: str) -> str:
        return f"https://www.youtube.com/watch?v={video_id}"

    def extract_playlist_id_from_url(self, playlist_url: str) -> str:
        pattern = r"(?<=list=)[\w-]+"
        match = re.search(pattern, playlist_url)
        if match:
            return match.group(0)
        else:
            return None
