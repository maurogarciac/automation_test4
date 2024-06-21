from seleniumpagefactory import PageFactory
from selenium import webdriver

from config.settings import Urls
from tests.ui.utils.locators import get_button_selector


class BasePage(PageFactory):
    """Shared methods applicable in all pages (allegedly)"""
    locators = {
        "storeButton": ('XPATH', get_button_selector("Store")),
        "cartButton": ('XPATH', get_button_selector("Cart")),
        "logOutButton": ('XPATH', get_button_selector("Log Out")),
    }

    def __init__(self, driver: webdriver) -> None:
        super().__init__()
        self.driver = driver

    def go_to(self):
        ...

    def click_store(self):
        ...

    def click_cart(self):
        ...

    def click_logout(self):
        ...
