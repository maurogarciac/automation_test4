import pytest
from datetime import datetime


# Reads flags and options
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute the automation")


# Reporting config
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


def pytest_html_report_title(report):
    report.title = datetime.date
