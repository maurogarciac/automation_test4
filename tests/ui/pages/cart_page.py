from selenium import webdriver

from tests.ui.pages.base_page import BasePage


class StorePage(BasePage):
    locators = {
        "inputPens": ('XPATH', "//input[@id='quantity-ASAPP Pens']"),
    }

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.driver = driver

    def click_empty_cart_button(self) -> None:
        ...

    def add_pens_to_cart(self, amount: int) -> None:
        ...

    def add_stickers_to_cart(self, amount: int) -> None:
        ...

    def add_water_bottles_to_cart(self, amount: int) -> None:
        ...

    def read_cart(self) -> None:
        ...
