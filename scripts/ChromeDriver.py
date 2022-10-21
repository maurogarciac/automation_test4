from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os



class ChromeDriver():

    def get_driver() -> webdriver:
        os.environ['WDM_LOG'] = str(logging.NOTSET)
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
