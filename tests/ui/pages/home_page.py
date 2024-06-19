from seleniumpagefactory import PageFactory
from selenium import webdriver
from config.settings import Urls
from tests.ui.pages.results_page import BaseResultPage


class HomePage(PageFactory):
    locators = {
        "input": ('NAME', 'q'),
        "submit": ('NAME', 'btnK'),
    }

    def __init__(self, driver: webdriver) -> None:
        super().__init__()
        self.driver = driver

    def go_to_page(self) -> None:
        self.driver.get(Urls.HOME_PAGE)

    def go_search(self, value: str) -> BaseResultPage:
        self.input.set_text(value)
        self.submit.click_button()
        return BaseResultPage(self.driver)
