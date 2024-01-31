# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from enum import Enum


class QualityPresetsBase(str, Enum):
    Q360P = "360p"
    Q480P = "480p"
    Q720P = "720p"
    Q1080P = "1080p"
    Q1440P = "1440p"
    Q2160P = "2160p"


class ConfigBase:
    def __init__(
        self,
        downloadsPath: str = "/downloads",
        updateFrequency: float = 15.0,
        maxComments: int = 500,
        preferredQuality: QualityPresetsBase = QualityPresetsBase.Q720P,
    ):
        self.downloadsPath = downloadsPath
        self.updateFrequency = updateFrequency
        self.maxComments = maxComments
        self.preferredQuality = preferredQuality
