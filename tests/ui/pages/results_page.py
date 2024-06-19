from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory
from selenium import webdriver

from tests.ui.utils.conditions.visibility import visibility_of_n_elements_located


class BaseResultPage(PageFactory):
    """Shared methods applicable in all result pages (allegedly)"""
    locators = {
        "resultTitle": ('CSS', '#rso div div[lang]')
    }

    LOAD_TIMEOUT: float = 5

    def __init__(self, driver: webdriver) -> None:
        super().__init__()
        self.driver = driver

    def find_urls(self, number: int) -> list:
        """ Scans a list of {number} web elements in the results list and returns their urls.

        :param number: Total number of urls expected

        :returns: A list of {number} urls for websites.
        """
        result_anchors = WebDriverWait(self.driver, timeout=self.LOAD_TIMEOUT) \
            .until(visibility_of_n_elements_located(self.locators["resultTitle"], number))
        # todo fix that it returns an empty list
        return [result.get_attribute('href') for result in result_anchors]
