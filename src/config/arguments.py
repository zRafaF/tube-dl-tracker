# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "--freq",
    default="15.0",
    help="[Initial setup only] Frequency (in minutes) for the tracker to check for new content. Default: 15 minutes",
)
parser.add_argument(
    "--downloads-path",
    default="/downloads",
    help="[Initial setup only] Path to download the contents. Default: /downloads",
)
parser.add_argument(
    "--host",
    default="127.0.0.1",
    help="Specify the host to run the web ui. Default: 127.0.0.1",
)
parser.add_argument(
    "--port",
    type=int,
    default=8000,
    help="Specify the port for the web ui. Default: 8000",
)
parser.add_argument(
    "--base-url",
    default="/",
    help="Specify the base path of ulr for the web ui. This is useful when running behind a reverse proxy.",
)
parser.add_argument(
    "-d",
    "--demo",
    action="store_true",
    help="Enables the demo mode. No content is downloaded and some features are disabled.",
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
