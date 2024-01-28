# Copyright (c) 2024 Rafael Farias
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import FastAPI, Request
from .scheduler import app_rocketry
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

GLOBALS = {
    "pages": [{
        'name': 'home',
        'url': '/'
    }, {
        'name': 'items',
        'url': 'items/1'
    }]
}

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
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.j2", context={"current_page": "home"}
    )


@app_fastapi.get("/items/{id}", response_class=HTMLResponse)
async def read_items(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="items.j2", context={"current_page": "items", "id": id}
    )