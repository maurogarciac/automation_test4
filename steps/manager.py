import subprocess
import pytest
from selenium import webdriver


class Manager():

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver


    def start(self) -> None:
        print(self.driver)
        #subprocess.run(". activate", cwd="\automation_test4\venv\Scripts")
        #subprocess.run("python -m pytest", cwd="\automation_test4")
        pytest.main(["-x", "steps"])   
    

    def get_driver(self) -> webdriver:
        return self.driver
