#!/usr/bin/env python

from typing import List
import sys


def run_tests(browser: List[str]) -> str:
    cmd_option = browser[1].lower()
    cmd_parameter = browser[2].lower()

    if cmd_option == "--browser" or cmd_option == "-b":
        if cmd_parameter == "firefox":
            #Run the FirefoxDriver class
            return "Running tests on Firefox web browser"
        elif cmd_parameter == "chrome":
            #Run the ChromeDriver class
            return "Running tests on Chrome web browser"
        return  """
                Please provide a valid browser parameter.\n
                The available browsers are:
                [Firefox, Chrome]
                """
    elif cmd_option == "--help" or cmd_option == "-h":
        return  """
                Usage: run_tests.py [OPTION] [PARAMETER]

                -b,  --browser       allows to pass a browser as a parameter
                -h,  --help          displays a list of all available options

                Long and short forms of options are interchangeable and have no
                effect in the funcionality of the script.
                Parameters are not mandatory, it depends on the option chosen.
                Options are mandatory.
                """
    else:
        return "Please provide a valid option, use the '--help' option for more information"

print(run_tests(sys.argv))
