import pytest, logging
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as F_Service
from selenium.webdriver.chrome.service import Service as C_Service
from pages.home_page import HomePage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

lg: logging.Logger = logging.getLogger(__name__)


# Reads flags and options
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute the automation")


@pytest.fixture(autouse=True)
def driver(request):
    global _driver
    browser = request.config.option.browser

    if browser == "firefox":
        _driver = webdriver.Firefox(service=F_Service(GeckoDriverManager().install()), service_log_path='./reports/geckodriver.log')
        lg.info("Started UI Tests with Firefox / Gecko driver")
    elif browser == "remote":
        capabilities = {
            'browserName': 'firefox',
            'javascriptEnabled': Truef
        }
        _driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=capabilities)
        # log.info here
    elif browser == "chrome_headless":
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--no-sandbox")
        _driver = webdriver.Chrome(service=C_Service(ChromeDriverManager().install()), options=opts)
        # log.info here
    elif browser == "chrome":
        _driver = webdriver.Chrome(service=C_Service(ChromeDriverManager().install()))
        # log.info here
    else:
        # log.error something here
        ...
    _driver.implicitly_wait(5)
    _driver.maximize_window()
    # log.info here
    yield _driver
    if request.node.rep_call.failed:
        screenshot_name = 'failed: %s' % datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        _driver.get_screenshot_as_png()
        # log.info here
    _driver.quit()


@pytest.fixture
# Adds page objects to local symbol table
def pages():
    home_page = HomePage(_driver)
    return locals()


# Reporting
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


def pytest_html_report_title(report):
    report.title = datetime.date
