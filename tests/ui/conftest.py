from logging import Logger, getLogger

import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as F_Service
from selenium.webdriver.chrome.service import Service as C_Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from tests.ui.pages.home_page import HomePage
from tests.ui.utils.screenshots import ScreenshotUtils

lg: Logger = getLogger(__name__)
IMPLICIT_TIMEOUT: float = 5


@pytest.fixture(autouse=True)
def driver(request: FixtureRequest):
    global _driver
    browser = request.config.option.browser

    if browser == "firefox":
        _driver = webdriver.Firefox(
            service=F_Service(GeckoDriverManager().install(), log_path='./reports/geckodriver.log'))
    elif browser == "remote":  # Not implemented to prioritize other requirements/features
        capabilities = {
            'browserName': 'firefox',
            'javascriptEnabled': True
        }
        _driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=capabilities)
    elif browser == "chrome_headless":
        op = webdriver.ChromeOptions()
        op.add_argument("--headless")
        op.add_argument("--disable-dev-shm-usage")
        op.add_argument("--no-sandbox")
        _driver = webdriver.Chrome(service=C_Service(ChromeDriverManager().install()), options=op)
    elif browser == "chrome":
        _driver = webdriver.Chrome(service=C_Service(ChromeDriverManager().install()))
    else:
        lg.error("Something's wrong initializing the web-driver! Fix it!")
    _driver.implicitly_wait(IMPLICIT_TIMEOUT)
    _driver.maximize_window()
    lg.info(f"Web Driver initialized as: {browser}")
    yield _driver
    if request.node.rep_call.failed:  # If the test fails, take a screenshot
        su: ScreenshotUtils = ScreenshotUtils()
        su.save_picture(request, _driver)
        lg.info(f"Error screenshot saved for {request.node.name}")
    _driver.quit()


@pytest.fixture
def pages():
    """
        Adds base page objects to local symbol table
    """
    home_page = HomePage(_driver)
    return locals()
