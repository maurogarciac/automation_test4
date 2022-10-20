from seleniumpagefactory import PageFactory
from typing import Any

class HomePage(PageFactory):
    
    locators = {
        "suggestion": ('XPATH','//*[@id="autocomplete"]'),
    }


    def __init__(self, driver):
        self.driver = driver
    

    def go_to(self) -> None:
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    def go_radio(self) -> None:              #Actually, this returns a Web Element, but there is no WebElement object on Selenium types apparently
        self.suggestion.set_text("Me")
        
