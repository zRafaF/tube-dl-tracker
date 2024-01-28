<!--
 Copyright (c) 2024 Rafael F. Meneses

 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Tube DL Tracker (TDT)

This is a piece of software that **tracks** and automatically **downloads** videos from a playlist.

## Use case

As you use YouTube and find a video you want to archive simply add it to a tracker playlist and it will be automatically downloaded.

## Settings

-   `freq`: Frequency of which the tracker will check for new content.
-   `path`: Download path of your videos
-   `playlists`: Array with the URL of the playlists you want to track.

## Downloaded content

TDT will Download the contents of a playlist to a folder with it's name

## CMD cheat sheet
* **Serve** website: Runs the uvicorn server with all the functionalities.
    * `python .\src\main.py`
* **Build static** website: Tries to render the Jinja2 templates for static hosting.
    * `python .\src\main.py -b`
* **Build static** website and **serves** it: Tries to render the Jinja2 templates for static hosting then serves locally.
    * `python .\src\main.py -s`

## About

### Web ui

Powered by FastAPI, and using [FastBootstrap](https://fastbootstrap.com/) for styling.
