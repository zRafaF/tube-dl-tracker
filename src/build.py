# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from service.api import app_fastapi, templates
from service.globals import GLOBALS

from fastapi import FastAPI
from fastapi.testclient import TestClient
import shutil
import subprocess
import os


def build_static(host: str, port: int):
    client = TestClient(app_fastapi)
    client.base_url = f"http://{host}:{port}"

    for page in GLOBALS.pages:
        response = client.get(page.url)

        if page.name == "home":
            path = f"build/index.html"
        else:
            path = f"build/{page.name}/index.html"

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            f.write(response.text)


def serve_static(host: str, port: int):
    # copy static files, and overwrite if exists
    shutil.copytree("static", "build/static", dirs_exist_ok=True)

    # run cmd on host and port
    subprocess.run(
        [
            "python",
            "-m",
            "http.server",
            str(port),
            "-b",
            str(host),
            "--directory",
            "build",
        ]
    )
