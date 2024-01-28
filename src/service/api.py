# Copyright (c) 2024 Rafael Farias
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import FastAPI, Request, Form

from config.schemas import ConfigBase
from .scheduler import app_rocketry
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from .schemas import *
from config import configurator
from .globals import GLOBALS
from .messages import messenger

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
        request=request, name="home.j2", context={"current_page": "home"}
    )


@app_fastapi.get("/settings", response_class=HTMLResponse)
async def get_settings(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="settings.j2",
        context={"current_page": "settings", "config": configurator.get_config()},
    )


@app_fastapi.post("/settings", response_class=HTMLResponse)
async def post_settings(
    request: Request, downloadsPath: str = Form(...), updateFrequency: str = Form(...)
):
    configurator.set_config(
        ConfigBase(downloadsPath=downloadsPath, updateFrequency=float(updateFrequency))
    )
    messenger.send_message("Updated completed!", MessageType.SUCCESS)

    return templates.TemplateResponse(
        request=request,
        name="settings.j2",
        context={
            "current_page": "settings",
            "config": configurator.get_config(),
        },
    )


@app_fastapi.get("/items/{id}", response_class=HTMLResponse)
async def get_items(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="items.j2", context={"current_page": "items", "id": id}
    )
