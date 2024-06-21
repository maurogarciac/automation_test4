from seleniumpagefactory import PageFactory
from selenium import webdriver

from config.settings import Urls
from tests.ui.pages.store_page import StorePage
from tests.ui.utils.locators import get_button_selector, get_contained_button_selector


class LoginPage(PageFactory):
    locators = {
        "inputUsername": ('ID', 'username'),
        "inputPassword": ('ID', 'password'),
        "submitLogInButton": ('XPATH', get_button_selector('Log In')),
        "registerButton": ('XPATH', get_button_selector('Register')),
        "inputRegisterUsername": ('ID', 'register-username'),
        "inputRegisterPassword": ('ID', 'register-password'),
        "submitRegistrationButton": ('XPATH', get_contained_button_selector('Register', '//div[contains(@class, "MuiDialog-root")]')),
    }

    def __init__(self, driver: webdriver) -> None:
        super().__init__()
        self.driver = driver

    def go_to_page(self) -> None:
        self.driver.get(f"{Urls.HOME_PAGE}/login")

    def do_register(self, new_username: str, new_password: str) -> None:
        self.registerButton.click_button()
        self.inputRegisterUsername.set_text(new_username)
        self.inputRegisterPassword.set_text(new_password)
        self.submitRegistrationButton()

    def do_login(self, username: str, password: str) -> StorePage:
        self.inputUsername.set_text(username)
        self.inputPassword.set_text(password)
        self.submitLogInButton.click_button()
        return StorePage(self.driver)
