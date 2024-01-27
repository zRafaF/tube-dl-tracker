# Copyright (c) 2024 Rafael F. Meneses
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from yt_dlp import YoutubeDL


# Function to list videos in a playlist
def list_playlist_videos(playlist_url):
    ydl_opts = {'extract_flat': True, 'verbose': True}
    with YoutubeDL(ydl_opts) as ydl:
        playlist_dict = ydl.extract_info(playlist_url, download=False)
        for entry in playlist_dict['entries']:
            video_title = entry['title']
            video_url = entry['url']
            print(f"{video_title}: {video_url}")

if __name__ == "__main__":
    playlist_url = 'https://www.youtube.com/playlist?list=PLCiNIjl_KpQhFwQA3G19w1nmhEOlZQsGF'
    list_playlist_videos(playlist_url)



