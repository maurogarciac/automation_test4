from seleniumpagefactory import PageFactory
from selenium import webdriver
from config.settings import Urls


class HomePage(PageFactory):
    locators = {
        "search": ('XPATH', '//*[@title="Search"]'),
    }

    def __init__(self, driver: webdriver) -> None:
        super().__init__()
        self.driver = driver

    def go_to_page(self) -> None:
        self.driver.get(Urls.HOME_PAGE)

    def go_search(self, value: str) -> None:
        self.suggestion.set_text(value)
