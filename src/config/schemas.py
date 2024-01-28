# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


class ConfigBase:
    def __init__(
        self, downloadsPath: str = "/downloads", updateFrequency: float = 30.0
    ):
        self.downloadsPath = downloadsPath
        self.updateFrequency = updateFrequency
