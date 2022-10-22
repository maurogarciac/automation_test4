#!/usr/bin/env python

from scripts.firefox_driver import FirefoxDriver
from scripts.chrome_driver import ChromeDriver

from typing import List
import sys

from steps.manager import Manager


def run_tests(browser: List[str]) -> str:
    invalid_opt_err =       "Please provide a valid option, use the '--help' option for more information"
    invalid_browser_err =   """
                            Please provide a valid browser parameter.\n
                            The available browsers are:
                            [Firefox, Chrome]
                            """

    if len(browser) > 1:
        
        cmd_option = browser[1].lower()

        if cmd_option == "--browser" or cmd_option == "-b":
            
            if len(browser) > 2:

                cmd_parameter = browser[2].lower()
            
                if cmd_parameter == "firefox":
                    #Run the FirefoxDriver class
                    Manager(FirefoxDriver.get_driver()).start()
                    return "Ran tests on Firefox web browser"
                elif cmd_parameter == "chrome":
                    #Run the ChromeDriver class
                    Manager(ChromeDriver.get_driver()).start()
                    return "Ran tests on Chrome web browser"
                else:
                    return invalid_browser_err
            else:
                return invalid_browser_err

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
            return invalid_opt_err
    else: 
        return invalid_opt_err
    
    

print(run_tests(sys.argv))
