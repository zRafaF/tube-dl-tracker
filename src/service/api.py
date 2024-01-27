# Copyright (c) 2024 Rafael Farias
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import FastAPI, Request
from .scheduler import app_rocketry

app_fastapi = FastAPI()

session = app_rocketry.session


@app_fastapi.get("/running-tasks")
async def get_tasks():
    """
    Current running rocketry tasks
    """
    return session.tasks


@app_fastapi.get("/")
async def read_root(request: Request):
    return {
        "message": "Hello World",
    }
