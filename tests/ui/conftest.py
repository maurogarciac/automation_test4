from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as F_Service
from selenium.webdriver.chrome.service import Service as C_Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from tests.ui.pages.home_page import HomePage


lg: logging.Logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def driver(request):
    global _driver
    browser = request.config.option.browser

    if browser == "firefox":
        _driver = webdriver.Firefox(service=F_Service(GeckoDriverManager().install(), log_path='./reports/geckodriver.log'))
    elif browser == "remote":
        capabilities = {
            'browserName': 'firefox',
            'javascriptEnabled': True
        }
        _driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=capabilities)
    elif browser == "chrome_headless":
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--no-sandbox")
        _driver = webdriver.Chrome(service=C_Service(ChromeDriverManager().install()), options=opts)
    elif browser == "chrome":
        _driver = webdriver.Chrome(service=C_Service(ChromeDriverManager().install()))
    else:
        lg.error("Something's wrong initializing the web-driver! Fix it!")
    _driver.implicitly_wait(5)
    _driver.maximize_window()
    lg.info(f"Web Driver initialized as: {browser}")
    yield _driver
    if request.node.rep_call.failed:
        ts: str = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        screenshot_name = 'failed-%s' % ts
        _driver.get_screenshot_as_png()
        lg.info(f"Error Screenshot taken, timestamp: {ts}")
        # todo replace with proper screenshot implementation
    _driver.quit()


@pytest.fixture
def pages():
    """
        Adds base page objects to local symbol table
    """
    home_page = HomePage(_driver)
    return locals()
