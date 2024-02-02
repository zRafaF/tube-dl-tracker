# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from loguru import logger

logger.add("logs/logs.log", retention=3, rotation="2 MB", level="INFO")

from service import api as service_api

import asyncio
import uvicorn
from service import (
    core as service_core,
    scheduler as service_scheduler,
)
from build import build_static, serve_static
from service.globals import GLOBALS
from config.arguments import args
from database import db
from ythandler import yt_handler

if args.base_url:
    GLOBALS.base_url = args.base_url
    logger.info(f"Base url set to {GLOBALS.base_url}")

if args.demo == True:
    GLOBALS.demo_mode = True
    logger.info("Demo mode enabled")

if args.build == True or args.static == True:
    logger.info("Building static website...")
    build_static(host=args.host, port=args.port)
    if args.static == True:
        logger.info("Serving static website...")
        serve_static(host=args.host, port=args.port)
    exit(0)


async def main():
    logger.info("Starting database...")
    db.start()
    logger.info("Starting server...")
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
