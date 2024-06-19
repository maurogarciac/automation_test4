from config.settings import Urls
from tests.ui.pages.home_page import HomePage
from tests.ui.pages.results_page import BaseResultPage
from logging import Logger, getLogger

lg: Logger = getLogger(__name__)


class TestUI:

    def test_1(self, pages, driver) -> None:
        home_page: HomePage = pages['home_page']
        home_page.go_to_page()
        assert Urls.HOME_PAGE in driver.current_url

    def test_2(self, pages, driver) -> None:
        home_page: HomePage = pages['home_page']
        home_page.go_to_page()
        assert Urls.HOME_PAGE in driver.current_url
        result_page: BaseResultPage = home_page.go_search('Fruit')
        result: list = result_page.find_urls(5)
        lg.info(result)
        assert len(result) == 5

    def test_that_fails(self, pages, driver):
        home_page: HomePage = pages['home_page']
        home_page.go_to_page()
        assert "error" == driver.current_url
