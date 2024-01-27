# Copyright (c) 2024 Rafael F. Meneses
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from argparse import ArgumentParser
import asyncio
import uvicorn
from service import core as service_core, api as service_api, scheduler as service_scheduler
import httpx
from loguru import logger


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
args = parser.parse_args()


async def main():
    logger.add("logs/logs.log", retention=3, rotation='2 MB', level="INFO")

    server = service_core.Server(
        config=uvicorn.Config(
            service_api.app_fastapi,
            workers=1,
            loop="asyncio",
            host=args.host,
            port=args.port,

        )
    )

    api_server = asyncio.create_task(server.serve())
    sched = asyncio.create_task(service_scheduler.app_rocketry.serve())

    await asyncio.wait([sched, api_server])


if __name__ == "__main__":
    asyncio.run(main())