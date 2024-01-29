# Copyright (c) 2024 Rafael Farias
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import FastAPI, Request, Form, status

from config.schemas import ConfigBase
from ythandler.raw_schemas import RawExtractedPlaylistBase
from .scheduler import app_rocketry
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from .schemas import *
from config import configurator
from .globals import GLOBALS
from .messages import messenger
from ythandler import yt_handler

app_fastapi = FastAPI()
app_fastapi.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

templates.env.globals["globals"] = GLOBALS


session = app_rocketry.session


@app_fastapi.get("/running-tasks")
async def get_tasks():
    """
    Current running rocketry tasks
    """
    return session.tasks


@app_fastapi.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.j2", context={"current_page": "Home"}
    )


@app_fastapi.get("/settings", response_class=HTMLResponse)
async def get_settings(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="settings.j2",
        context={"current_page": "Settings", "config": configurator.get_config()},
    )


@app_fastapi.post("/settings", response_class=RedirectResponse)
async def post_settings(
    request: Request, downloadsPath: str = Form(...), updateFrequency: str = Form(...)
):
    configurator.set_config(
        ConfigBase(downloadsPath=downloadsPath, updateFrequency=float(updateFrequency))
    )
    messenger.send_message("Updated completed!", MessageType.SUCCESS)

    # Redirects to the get page so it doesn't triggers a post request again
    return RedirectResponse(url="/settings", status_code=status.HTTP_303_SEE_OTHER)


@app_fastapi.get("/add-playlist/{id}", response_class=HTMLResponse)
async def get_items(request: Request, id: str):
    (playlist, execution_time) = yt_handler.get_playlist_info(id)

    messenger.send_message(
        f"Playlist data fetched successfully! Took {execution_time:.2f}s.",
        MessageType.SUCCESS,
    )

    return templates.TemplateResponse(
        request=request,
        name="add-playlist.j2",
        context={"current_page": "Add Playlist", "playlist": playlist},
    )


@app_fastapi.post("/api/submit-url", response_class=RedirectResponse)
async def get_items(request: Request, submittedUrl: str = Form(...)):
    id = yt_handler.extract_playlist_id_from_url(submittedUrl)

    if id is None:
        messenger.send_message(
            f"Invalid playlist URL, couldn't find list id.", MessageType.DANGER
        )
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    return RedirectResponse(
        url=f"/add-playlist/{id}",
        status_code=status.HTTP_303_SEE_OTHER,
    )
