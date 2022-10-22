from seleniumpagefactory import PageFactory

class IFramePage(PageFactory):
    
    locators = {

    }
    
    def __init__(self, driver):
        self.driver = driver
    