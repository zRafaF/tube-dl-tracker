# Copyright (c) 2024 Rafael Farias
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from rocketry import Rocketry
from rocketry.conds import every
from loguru import logger

app_rocketry = Rocketry()


@app_rocketry.task(every("10 minutes"))
def check_schedule_health():
    """
    Scheduler health check
    """
    logger.debug("Scheduler health check")


@app_rocketry.task(every("15 minutes"))
def run_tracker():
    """
    Tracks the playlists for new content
    """


def reschedule_tracker_task(new_freq_minutes: float):
    """
    Reschedule tasks
    """
    freq = f"{new_freq_minutes} minutes"
    app_rocketry.session[run_tracker].start_cond = every(freq)
    logger.success(f"Tracker frequency set to every ({freq})")
