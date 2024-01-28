# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from loguru import logger

logger.add("logs/logs.log", retention=3, rotation="2 MB", level="INFO")

from argparse import ArgumentParser
import asyncio
import uvicorn
from service import (
    core as service_core,
    api as service_api,
    scheduler as service_scheduler,
)
from build import build_static, serve_static


parser = ArgumentParser()
parser.add_argument(
    "--freq",
    default="0.1",
    help="Frequency (in minutes) for the tracker to check for new content",
)
parser.add_argument(
    "--host", default="127.0.0.1", help="Specify the host to run the web ui"
)
parser.add_argument(
    "--port", type=int, default=8000, help="Specify the port for the web ui"
)
parser.add_argument(
    "--path",
    default="/tube-dl-tracker",
    help="Specify the root path to run FastAPI app",
)
parser.add_argument(
    "-b",
    "--build",
    action="store_true",
    help="Builds the static website and exits. The website will be available at /build",
)
parser.add_argument(
    "-s",
    "--static",
    action="store_true",
    help="Serve the static website.",
)
args = parser.parse_args()

if args.build == True or args.static == True:
    build_static(host=args.host, port=args.port)
    if args.static == True:
        serve_static(host=args.host, port=args.port)
    exit(0)


async def main():
    server = service_core.Server(
        config=uvicorn.Config(
            service_api.app_fastapi,
            workers=1,
            loop="asyncio",
            host=args.host,
            port=args.port,
            reload=True,
            reload_includes=["*.html", "*.js", "*.css", "*.png", "*.ico"],
            reload_excludes=["static/fastbootstrap-2.2.0"],
        )
    )

    api_server = asyncio.create_task(server.serve())
    sched = asyncio.create_task(service_scheduler.app_rocketry.serve())
    await asyncio.wait([sched, api_server])


if __name__ == "__main__":
    asyncio.run(main())
