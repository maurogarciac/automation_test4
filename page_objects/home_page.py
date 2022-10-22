from seleniumpagefactory import PageFactory
from typing import Any
from selenium import webdriver


base_url = "https://rahulshettyacademy.com/AutomationPractice/"

class HomePage(PageFactory):
    
    locators = {
        "suggestion": ('XPATH','//*[@id="autocomplete"]'),
    }


    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
    

    def go_to_page(self) -> None:
        self.driver.get(base_url)

    def go_radio(self) -> None:
        self.suggestion.set_text("Me")
        
