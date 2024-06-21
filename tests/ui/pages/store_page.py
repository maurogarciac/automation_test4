from selenium import webdriver

from tests.ui.pages.base_page import BasePage


class StorePage(BasePage):
    locators = {
        "inputPens": ('XPATH', "//input[@id='quantity-ASAPP Pens']"),
        "inputStickers": ('XPATH', "//input[@id='quantity-ASAPP Stickers']"),
        "inputWaterBottles": ('XPATH', "//input[@id='quantity-ASAPP Water Bottle']"),
        "buttonAddPensToCart": ('XPATH', "//*[contains(text(),'ASAPP Pens')]/../../..//ancestor::button[*[contains(text(),'Add to Cart')]]"),
        "buttonAddStickersToCart": ('XPATH', "//*[contains(text(),'ASAPP Stickers')]/../../..//ancestor::button[*[contains(text(),'Add to Cart')]]"),
        "buttonAddBottlesToCart": ('XPATH', "//*[contains(text(),'ASAPP Water Bottle')]/../../..//ancestor::button[*[contains(text(),'Add to Cart')]]"),
    }

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.driver = driver

    def add_pens_to_cart(self, amount: int) -> None:
        ...

    def add_stickers_to_cart(self, amount: int) -> None:
        ...

    def add_water_bottles_to_cart(self, amount: int) -> None:
        ...
