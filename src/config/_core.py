# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import json
from .schemas import ConfigBase
from loguru import logger
from .arguments import args


class Configurator:
    def __init__(self, config_file: str = "config.json"):
        self._config_file = config_file
        self._config = self._load_config()
        self.VERSION = "0.0.1"

    def get_config(self) -> ConfigBase:
        return self._config

    def set_config(self, config: ConfigBase) -> None:
        self._config = config
        self._save_config(self._config)

    def _load_config(self) -> ConfigBase:
        try:
            with open(self._config_file, "r") as file:
                config_data = json.load(file)
                logger.info(f"Config file '{self._config_file}' was found, parsing...")
                config = ConfigBase(**config_data)
                logger.success(
                    f"Config file '{self._config_file}' parsed successfully."
                )
                return config
        except FileNotFoundError:
            try:
                logger.warning(
                    f"Error: File '{self._config_file}' not found. Creating one..."
                )
                config_default = ConfigBase(args.downloads_path, float(args.freq))
                with open(self._config_file, "w") as file:
                    json.dump(config_default.__dict__, file, indent=4)
                logger.success(f"Config file '{self._config_file}' created.")
                return config_default
            except Exception as e:
                logger.error(f"Error creating config file '{self._config_file}'.")
                logger.error(e)
                raise e
        except json.JSONDecodeError:
            logger.error(f"Error: Unable to decode JSON from '{self._config_file}'.")
            return None
        except KeyError:
            logger.error(f"Error: Unable to parse config file '{self._config_file}'.")
            return None
        except Exception as e:
            logger.error(f"Error loading config file '{self._config_file}'.")
            logger.error(e)
            raise e

    def _save_config(self, config: ConfigBase) -> None:
        if config is None:
            return
        try:
            with open(self._config_file, "w") as file:
                json.dump(config.__dict__, file, indent=4)
                logger.success(f"Config saved to {self._config_file} successfully.")
        except Exception as e:
            logger.error(
                f"Error: Unable to save config to {self._config_file}. Reason: {e}"
            )
