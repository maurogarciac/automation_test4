from seleniumpagefactory import PageFactory
from selenium import webdriver
from config.settings import Urls


class BasePage(PageFactory):
    """Shared methods applicable in all pages (allegedly)"""
    locators = {}

    def __init__(self, driver: webdriver) -> None:
        super().__init__()
        self.driver = driver
