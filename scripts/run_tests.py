#!/usr/bin/env python

from typing import List
import sys


def run_tests(browser: List[str]) -> str:
    if browser[1].lower() == "--browser" or browser[1].lower() == "-b":
        if browser[2].lower() == "firefox":
            return "Running tests on Firefox web browser"
        elif browser[2].lower() == "chrome":
            return "Running tests on Chrome web browser"
        return  """
                Please provide a valid browser parameter.\n
                The available browsers are:
                [Firefox, Chrome]
                """
    if browser[1].lower() == "--help" or browser[1].lower() == "-h":
        return  """
                Usage: run_tests.py [OPTION] [PARAMETER]
                
                -b,  --browser       allows to pass a browser as a parameter
                -h,  --help          displays a list of all available options

                Long and short forms of options are interchangeable and have no
                effect in the funcionality of the script.
                Parameters are not mandatory, it depends on the option chosen.
                """
    else:
        return "Please provide a valid option, use the '--help' for more information" 

print(run_tests(sys.argv))
