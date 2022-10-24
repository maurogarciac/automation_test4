from selenium import webdriver


class Manager():

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver


    def start(self) -> None:
        print(self.driver)
        #pytest.main(["-x", "steps"])   
    

    def get_driver(self) -> webdriver:
        return self.driver
