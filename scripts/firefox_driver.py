from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxDriver():

    def get_driver() -> webdriver:
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
