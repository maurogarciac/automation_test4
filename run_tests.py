#!/usr/bin/env python

from typing import List
import sys


def run_tests(browser: List[str]) -> str:
    if browser[1].lower() == "firefox":
        return "Running tests on Firefox web browser"
    elif browser[1].lower() == "chrome":
        return "Running tests on Chrome web browser"
    return  """
            Please provide a valid browser option.\n
            The available browsers are:
            [Firefox, Chrome]
            """

print(run_tests(sys.argv))
