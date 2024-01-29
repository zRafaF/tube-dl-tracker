# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import re


def extract_list_id(url: str) -> str | None:
    """
    Extracts the list id from a youtube playlist url
    """
    pattern = r"(?<=list=)[\w-]+"
    match = re.search(pattern, url)
    if match:
        return match.group(0)
    else:
        return None
